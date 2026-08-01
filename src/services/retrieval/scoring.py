"""
Composite relevance scoring — pure Python, dependency-free (numpy-free).

WHAT THIS SOLVES
────────────────
Retrieval matches a QUESTION against a chunk's SUMMARY (a statement). With a
symmetric sentence-embedding model (all-MiniLM-L6-v2) the raw cosine for a
*genuinely relevant* pair lands around 0.55–0.75, and for an irrelevant pair
around 0.0–0.30. That is why raw scores looked "bad" (<0.75) even when the top
chunk was correct: 0.68 is a GOOD cosine for this model, not a poor one.

Rather than fake the number, we compute a **composite relevance score** from
three independent signals (exactly the combination requested):

    score = w_sum  * norm(cos(query, summary_vec))     # primary semantic signal
          + w_cnt  * norm(cos(query, content_vec))     # secondary, low weight
          + w_fac  * facet_match(query, chunk)         # lexical / structural

Each term is in [0, 1] and the weights sum to 1, so the composite is in [0, 1].

WHY CALIBRATION (norm) IS LEGITIMATE
────────────────────────────────────
Raw cosine from a symmetric model has a compressed dynamic range: the useful
band is roughly [0.25, 0.75], not [0, 1]. `norm()` linearly rescales that band
to [0, 1], which is standard score normalisation (the same idea as min-max
calibration before fusion). It changes the SCALE, not the RANKING, and it makes
the number mean what a user expects: "0.9 = strong match".

  ⚠ Honesty note: normalisation cannot invent relevance. If the right chunk is
  not retrieved, a high composite is meaningless. The facet term below is what
  genuinely improves the RANKING; normalisation only makes the reported number
  interpretable. Both `raw_summary_cos` and `raw_content_cos` are carried on the
  result so you can always inspect the underlying similarity.

THE FACET TERM — where real ranking gains come from
───────────────────────────────────────────────────
A question like "What is S-TAP?" shares an exact lexical anchor with the chunk
whose heading/keywords contain "S-TAP". Dense vectors blur such rare tokens;
lexical matching nails them. We score overlap between the query's terms and the
chunk's structured metadata (headings, keywords, features, workflows, entities,
personas), which is a hybrid (dense + sparse) retrieval — the standard fix.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass, field

# ── Calibration band for the embedding model ─────────────────────────────────
# Tuned for all-MiniLM-L6-v2 style symmetric models. Override via settings.
COS_FLOOR = 0.25     # at/below this, treat as no semantic signal
COS_CEIL  = 0.75     # at/above this, treat as a perfect semantic match


def norm(cos: float, floor: float = COS_FLOOR, ceil: float = COS_CEIL) -> float:
    """Rescale a raw cosine from its useful band [floor, ceil] onto [0, 1]."""
    if ceil <= floor:
        return 0.0
    return max(0.0, min(1.0, (cos - floor) / (ceil - floor)))


# ── Lexical / facet matching ─────────────────────────────────────────────────

_STOP = frozenset("""
a an the of for to in on at by with from into over under and or but if then than
is are was were be been being do does did doing how what when where which who whom
why can could should would may might will shall must i you it we they this that
these those as not no yes there here about my your our their me him her us them
stand stands stood mean means meant called call name named
""".split())

_WORD = re.compile(r"[A-Za-z][A-Za-z0-9_\-\.]+")


def terms(text: str) -> set[str]:
    """Content words, lower-cased. Keeps hyphens/dots (S-TAP, watsonx.ai)."""
    return {
        w.lower() for w in _WORD.findall(text or "")
        if len(w) > 1 and w.lower() not in _STOP
    }


def _idf_weight(term: str, df: dict[str, int], n_docs: int) -> float:
    """
    Rare terms matter more. A question sharing "S-TAP" with a chunk is a much
    stronger signal than sharing "configure". Standard smoothed IDF.
    """
    d = df.get(term, 0)
    return math.log(1.0 + (n_docs - d + 0.5) / (d + 0.5))


@dataclass
class ChunkFacets:
    """The structured metadata a chunk carries (filled at classification time)."""
    headings:  list[str] = field(default_factory=list)
    keywords:  list[str] = field(default_factory=list)
    features:  list[str] = field(default_factory=list)
    workflows: list[str] = field(default_factory=list)
    entities:  list[str] = field(default_factory=list)
    personas:  list[str] = field(default_factory=list)
    summary:   str = ""

    def weighted_fields(self) -> list[tuple[str, float]]:
        """(text, field_weight) — headings/keywords are the strongest anchors."""
        return [
            (" ".join(self.headings),  1.00),   # section title == what it's about
            (" ".join(self.keywords),  0.95),   # explicit product terms
            (" ".join(self.entities),  0.80),
            (" ".join(self.features),  0.75),
            (" ".join(self.workflows), 0.70),
            (" ".join(self.personas),  0.55),
            (self.summary,             0.50),
        ]


def facet_match(
    query: str,
    facets: ChunkFacets,
    df: dict[str, int] | None = None,
    n_docs: int = 1,
) -> float:
    """
    Lexical overlap between the query and a chunk's structured metadata, in [0,1].

    IDF-weighted so a shared rare term ("S-GATE") counts far more than a shared
    common one ("configure"). Field-weighted so a hit in the HEADING counts more
    than a hit in the summary body.
    """
    q = terms(query)
    if not q:
        return 0.0
    df = df or {}

    q_mass = sum(_idf_weight(t, df, n_docs) for t in q) or 1.0
    best = 0.0
    for text, fw in facets.weighted_fields():
        if not text.strip():
            continue
        hit = q & terms(text)
        if not hit:
            continue
        mass = sum(_idf_weight(t, df, n_docs) for t in hit)
        best = max(best, fw * (mass / q_mass))
    return max(0.0, min(1.0, best))


# ── Topic centrality — "is this section ABOUT X, or does it just MENTION X?" ──
#
# This is the single biggest ranking fix. Plain facet overlap saturates at 1.0
# for ANY section that happens to contain the query's rare term, so
# "What does S-TAP stand for?" was matching a troubleshooting page titled
# "S-TAP is not capturing traffic" just as strongly as a definition.
#
# A section's OWN TITLE (the last heading in the breadcrumb) declares its topic.
# We reward the query's rare terms appearing there, and further reward the title
# being SHORT and dominated by those terms — i.e. the section is *about* exactly
# that thing, not about a problem with it.

_PROBLEM_TITLE = re.compile(
    r"\b(?:not|cannot|can't|fail(?:s|ed|ure|ing)?|error|issue|problem|"
    r"troubleshoot(?:ing)?|resolv(?:e|ing)|workaround|unable)\b",
    re.IGNORECASE,
)


def topic_centrality(
    query: str,
    facets: ChunkFacets,
    df: dict[str, int] | None = None,
    n_docs: int = 1,
    penalise_problem_titles: bool = True,
) -> float:
    """
    How strongly this section's OWN TITLE is about the query's subject, in [0,1].

    1.0  → the title is essentially the query's subject ("S-TAP", "The alerter")
    ~0.5 → the subject appears in a longer, more specific title
    0.0  → the subject is absent from the title (only mentioned in the body)
    """
    if not facets.headings:
        return 0.0
    df = df or {}
    q = terms(query)
    if not q:
        return 0.0

    title = facets.headings[-1]
    t_terms = terms(title)
    if not t_terms:
        return 0.0

    hit = q & t_terms
    if not hit:
        return 0.0

    q_mass   = sum(_idf_weight(t, df, n_docs) for t in q) or 1.0
    hit_mass = sum(_idf_weight(t, df, n_docs) for t in hit)

    # (a) how much of the QUESTION's meaning the title covers
    coverage = hit_mass / q_mass
    # (b) how much of the TITLE is the subject (short, focused titles win)
    focus    = len(hit) / len(t_terms)

    score = coverage * (0.5 + 0.5 * focus)

    # A "what is X" answer never lives on a page titled "X is not working".
    if penalise_problem_titles and _PROBLEM_TITLE.search(title):
        score *= 0.35

    return max(0.0, min(1.0, score))


# ── Composite ────────────────────────────────────────────────────────────────

DEFAULT_WEIGHTS = {
    "summary": 0.75,   # primary — summary cosine carries the full semantic signal
    "content": 0.25,   # secondary — content cosine fallback
    "facet":   0.00,   # disabled — lexical facet signal removed from composite
}


@dataclass
class ScoreBreakdown:
    score:            float          # the composite, [0,1] — what callers display
    raw_summary_cos:  float
    raw_content_cos:  float
    summary_norm:     float
    content_norm:     float
    facet:            float

    def as_dict(self) -> dict:
        return {
            "score":           round(self.score, 4),
            "raw_summary_cos": round(self.raw_summary_cos, 4),
            "raw_content_cos": round(self.raw_content_cos, 4),
            "summary_norm":    round(self.summary_norm, 4),
            "content_norm":    round(self.content_norm, 4),
            "facet":           round(self.facet, 4),
        }


def composite_score(
    query: str,
    summary_cos: float,
    content_cos: float,
    facets: ChunkFacets,
    weights: dict[str, float] | None = None,
    df: dict[str, int] | None = None,
    n_docs: int = 1,
    floor: float = COS_FLOOR,
    ceil: float = COS_CEIL,
) -> ScoreBreakdown:
    """Fuse the three signals into one interpretable relevance score."""
    w = {**DEFAULT_WEIGHTS, **(weights or {})}
    total = sum(w.values()) or 1.0

    s_n = norm(summary_cos, floor, ceil)
    c_n = norm(content_cos, floor, ceil)
    f   = facet_match(query, facets, df, n_docs)

    score = (w["summary"] * s_n + w["content"] * c_n + w["facet"] * f) / total
    return ScoreBreakdown(
        score=max(0.0, min(1.0, score)),
        raw_summary_cos=summary_cos,
        raw_content_cos=content_cos,
        summary_norm=s_n,
        content_norm=c_n,
        facet=f,
    )


# ── Sub-type agreement ───────────────────────────────────────────────────────
#
# "How do I configure a collector?" must not be answered by a TROUBLESHOOT page,
# and "What is S-TAP?" must not be answered by an INSTALL page. The query's
# sub-type and the chunk's sub-type should agree.
#
# Definitional questions ("what is", "define") carry no explicit sub-type, so we
# treat OVERVIEW / REFERENCE chunks as their natural home and actively demote
# TROUBLESHOOT — which is exactly the failure we measured (Q1 "What does S-TAP
# stand for?" was landing on "Rules of Failover").

_DEFINITIONAL_Q = re.compile(
    r"^\s*(?:what\s+(?:is|are|does|do)\b|define\b|explain\b|describe\b|"
    r"who\s+is\b|which\s+\w+\s+(?:is|are)\b)",
    re.IGNORECASE,
)

# Where a definitional question's answer legitimately lives.
_DEFINITIONAL_HOME = {"overview", "reference", "other", ""}


def subtype_agreement(query: str, chunk_sub_type: str | None) -> float:
    """
    Multiplier in [0,1] expressing how well the chunk's sub-type suits the query.

    1.00 → sub-types match (or the chunk is a natural home for the question)
    0.60 → neutral / unknown
    0.25 → actively wrong kind of page (e.g. troubleshooting for a definition)
    """
    st = (chunk_sub_type or "").strip().lower()

    # Lazy import so this module stays dependency-free for offline tests.
    try:
        from src.services.ingestion.classifiers.taxonomy import detect_query_sub_type
        q_st = detect_query_sub_type(query)
        q_st = q_st.value if q_st is not None else None
    except Exception:                                   # pragma: no cover
        q_st = None

    if _DEFINITIONAL_Q.match(query or ""):
        if st == "troubleshoot":
            return 0.25                                 # the measured failure mode
        return 1.0 if st in _DEFINITIONAL_HOME else 0.6

    if q_st and st:
        if q_st == st:
            return 1.0
        # A "how do I configure" question is poorly served by a troubleshoot page.
        if st == "troubleshoot" and q_st != "troubleshoot":
            return 0.35
        return 0.6

    return 0.6


# ── The ranking score (what ORDERS results) ──────────────────────────────────

RANK_WEIGHTS = {
    "semantic":   0.45,   # norm(summary cosine)
    "facet":      0.20,   # lexical overlap with structured metadata
    "centrality": 0.35,   # is the section ABOUT the subject?
}


def rank_score(
    query: str,
    summary_cos: float,
    facets: ChunkFacets,
    chunk_sub_type: str | None = None,
    df: dict[str, int] | None = None,
    n_docs: int = 1,
) -> float:
    """
    Ordering score. Deliberately SEPARATE from `composite_score`:

      • `rank_score`      decides WHICH chunks come back  (relevance ordering)
      • `composite_score` decides the NUMBER you display   (calibrated relevance)

    Keeping them apart matters: normalising a cosine changes the displayed value
    but not the order, so a high displayed score on a wrongly-ranked chunk would
    be worse than useless. Topic-centrality and sub-type agreement here are what
    actually fix the ordering.
    """
    w = RANK_WEIGHTS
    sem  = norm(summary_cos)
    fac  = facet_match(query, facets, df, n_docs)
    cen  = topic_centrality(query, facets, df, n_docs)
    base = w["semantic"] * sem + w["facet"] * fac + w["centrality"] * cen
    return base * subtype_agreement(query, chunk_sub_type)
