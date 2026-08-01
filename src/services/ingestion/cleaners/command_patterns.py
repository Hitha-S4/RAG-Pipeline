"""
Generic command / API-reference regex patterns — DATA-SOURCE INDEPENDENT.

Derived by studying the structure of GDP 12.x pages 1064–1764 ("Deploying
Guardium on a cloud service" → "GuardAPI and REST API commands"), but every
pattern keys on the *shape* of reference content, never on a product noun.
There is no "grdapi", no "Guardium", no "GDP" anywhere below — swap in an
Oracle, ServiceNow, or Kubernetes manual and these still fire.

────────────────────────────────────────────────────────────────────────────
The anatomy the patterns exploit
────────────────────────────────────────────────────────────────────────────
A command-reference entry in *any* enterprise manual looks like this:

    add_assessment_datasource            ← ENTRY_HEADING   (bare snake_case id)
      This command adds a datasource…    ← prose (KEEP if you only strip cmds)
    REST API syntax                      ← SYNTAX_SECTION
      POST https://host:8443/restAPI/x   ← REST_CALL
    GuardAPI syntax                      ← SYNTAX_SECTION
      add_assessment_datasource parameter=value   ← SYNTAX_TEMPLATE
    Parameters                           ← PARAM_SECTION
      Parameter   Value type   Description        ← PARAM_TABLE_HEADER
    Example                              ← EXAMPLE_SECTION
      grdapi add_assessment_datasource a=1 b=2    ← CLI_INVOCATION

Six recurring shapes → six regexes. Combine them for block-level or
chapter-level stripping.
"""
from __future__ import annotations

import re

# ══════════════════════════════════════════════════════════════════════════════
# 1. CLI_INVOCATION — a command token followed by ≥2 key=value arguments.
#
#    matches:  grdapi add_datasource type=oracle name=myOra host=h1
#              aws ec2 run-instances --count=2 --type=t2.micro
#              kubectl set env deploy/app KEY=v1 OTHER=v2
#    rejects:  "The default value x=1 is used."      (prose: only 1 assignment)
#              "Set a=1 and b=2 in the file."        (leading token is prose)
#
#    Generic because it requires ARGUMENT DENSITY, not a known command name.
# ══════════════════════════════════════════════════════════════════════════════
CLI_INVOCATION = re.compile(
    r"""
    ^[ \t]*                           # start of line
    (?P<cmd>[a-z][\w.\-]*)            # command token: lowercase-initial, no spaces
    (?:\s+[a-z][\w./\-]*){0,3}        # up to 3 sub-commands ("ec2 run-instances",
                                      #   "set env deployment/app")
    (?:\s+(?:-{1,2}[\w-]+\s*)?        # ─┐ optional flag prefix  -f / --flag
        [\w.\-]+\s*=\s*               #  │  key =
        (?:"[^"]*"|'[^']*'|\S+)       #  │  "quoted" | 'value' | bare-token
    ){2,}                             # ─┘ ≥2 CONSECUTIVE assignments ← discriminator
    """,
    re.VERBOSE,
)
# ── Why no `$` anchor ────────────────────────────────────────────────────────
# Anchoring the assignments to end-of-line broke real commands with trailing
# positional args (`docker run --name=web --env=PROD image`). The end anchor was
# never what made this precise — the ≥2 *CONSECUTIVE* assignments are. Prose like
# "Set a=1 and b=2 in the file." still fails, because the word "and" interrupts
# the run, so it never reaches two back-to-back assignments.

# ══════════════════════════════════════════════════════════════════════════════
# 2. REST_CALL — an HTTP verb followed by a URL or an absolute path.
#
#    matches:  POST https://[hostname]:8443/restAPI/assessment_datasource
#              GET /api/v2/things?id=3
#              DELETE  http://host/x
#    rejects:  "POST the form to your admin."        (no path/URL follows)
# ══════════════════════════════════════════════════════════════════════════════
REST_CALL = re.compile(
    r"""
    ^\s*
    (?P<verb>GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)
    \s+
    (?P<target>
        https?://\S+                  # absolute URL
      | /[\w\-./{}\[\]]+               # absolute path (incl. {id} / [host] placeholders)
    )
    """,
    re.VERBOSE | re.IGNORECASE,
)

# ══════════════════════════════════════════════════════════════════════════════
# 3. SYNTAX_TEMPLATE — the abstract call signature, using literal placeholders.
#
#    matches:  add_assessment_datasource parameter=value
#              create_thing key=<value>
#              foo --name=<NAME>
#    This is the giveaway line of a reference entry: the *value* is the literal
#    word "value"/"<...>", not real data.
# ══════════════════════════════════════════════════════════════════════════════
SYNTAX_TEMPLATE = re.compile(
    r"""
    ^\s*
    [\w.\-]+                          # command name
    (?:\s+[\w.\-]+)*?                 # optional sub-commands
    \s+
    (?:-{0,2}[\w.\-]+\s*=\s*          # key =
        (?:
            <[^>]+>                   #   <placeholder>
          | \[[^\]]+\]                #   [placeholder]
          | value | VALUE             #   the literal word "value"
        )
        \s*
    )+
    $
    """,
    re.VERBOSE,
)

# ══════════════════════════════════════════════════════════════════════════════
# 4. SYNTAX_SECTION — the heading that introduces a call signature.
#
#    matches:  "REST API syntax" · "GuardAPI syntax" · "CLI syntax"
#              "Command syntax"  · "Synopsis" · "Usage"
#    Generic: any word(s) + "syntax", or the classic man-page section names.
# ══════════════════════════════════════════════════════════════════════════════
SYNTAX_SECTION = re.compile(
    r"^\s*(?:[\w\-/ ]{0,30}\bsyntax\b|synopsis|usage)\s*:?\s*$",
    re.IGNORECASE,
)

# ══════════════════════════════════════════════════════════════════════════════
# 5. PARAM_TABLE_HEADER — the column header of a parameter table.
#
#    matches:  "Parameter    Value type    Description"
#              "Name   Type   Required   Description"
#    rejects:  "the parameter type is described below"   (prose: single spaces)
#
#    Requires ≥2 COLUMN GAPS (runs of 2+ spaces) — the columnar layout that
#    survives `pdftotext -layout`. Prose uses single spaces, so this is what
#    separates a table header from a sentence containing the same words.
#
#    ⚠ CORROBORATING EVIDENCE ONLY. Measured against 40k lines of ordinary
#    prose, this still fires on legitimate config tables ("GIM parameter |
#    Description", "Run-Time Parameter | Operator | Default Value") that you
#    almost certainly want to KEEP. Never strip on this pattern alone — use it
#    only to confirm a block already flagged by CLI_INVOCATION / REST_CALL /
#    SYNTAX_TEMPLATE.
# ══════════════════════════════════════════════════════════════════════════════
PARAM_TABLE_HEADER = re.compile(
    r"""
    ^\s*
    (?=(?:.*\b(?:parameter|argument|field|name|key|option)s?\b))       # a "name" column
    (?=(?:.*\b(?:description|value\s*type|type|required|default)\b))   # a "meta" column
    (?=(?:.*\S\s{2,}\S.*\S\s{2,}\S))                                   # ≥2 column gaps
    [\w\s|/()\-]{5,120}
    $
    """,
    re.VERBOSE | re.IGNORECASE,
)

# ══════════════════════════════════════════════════════════════════════════════
# 6. ENTRY_HEADING — a bare identifier alone on a line: the command's own name.
#
#    matches:  "add_assessment_datasource"  ·  "create-thing"  ·  "listUsers"
#    rejects:  "Deploying the agent"  (has a space → it's prose/heading)
#              "Note"                 (too short / common word — see _STOPWORDS)
#
#    Only meaningful in combination with the others (a lone identifier is weak
#    evidence); use as a boundary marker for splitting entries.
# ══════════════════════════════════════════════════════════════════════════════
ENTRY_HEADING = re.compile(r"^\s*(?P<name>[a-z][a-z0-9]*(?:[_\-][a-z0-9]+){1,6})\s*$", re.IGNORECASE)

# ══════════════════════════════════════════════════════════════════════════════
# 7. REFERENCE_CHAPTER_HEADING — chapter-level boundary (for whole-chapter cuts).
#
#    matches:  "GuardAPI and REST API commands"
#              "REST API reference" · "Command reference" · "Appendix B. CLI commands"
#    rejects:  "Ignore SQL commands"                      (no API/CLI term)
#              "For more information, see ... report."    (sentence, ends with '.')
#              "SQL commands are filtered at the"         (sentence fragment)
#
#    ── Bug this design avoids ──────────────────────────────────────────────
#    A naive version used two lookaheads whose word-lists OVERLAPPED
#    ("commands" appeared in both), so a single word satisfied both and the
#    prose line "Ignore SQL commands" matched. The two vocabularies below are
#    DISJOINT, so a real heading must carry two independent signals:
#        (a) an interface term   — api / cli / rest / sdk
#        (b) a reference term    — command(s) / reference / syntax / call(s)
#    …plus heading SHAPE: no trailing sentence punctuation, starts uppercase,
#    short, and contains no sentence connectives.
# ══════════════════════════════════════════════════════════════════════════════
REFERENCE_CHAPTER_HEADING = re.compile(
    r"""
    ^[ \t]*
    (?:appendix\s+[A-Z0-9]+[.:]?\s*)?              # optional "Appendix B."
    (?=(?-i:[A-Z0-9]))                             # heading starts UPPERCASE (see note)
    (?=                                            # (a) interface qualifier — EITHER…
        .*\b(?:api|apis|cli|rest|sdk)\b            #     an interface term, OR
      | .*\bcommands?\s+(?:reference|syntax)\b     #     the phrase "command reference"
    )
    (?=.*\b(?:commands?|reference|syntax|calls?)\b)  # (b) reference term  ← disjoint
    (?!.*\b(?:see|refer|following|example|note|for\ more\ information)\b)  # not a sentence
    (?![^\n]*\S\s{2,}\S)                           # not a table row (no column gaps)
    [\w\s\-&/,.]{5,70}
    (?<![.:;!?])                                   # no trailing sentence punctuation
    [ \t]*$
    """,
    re.VERBOSE | re.IGNORECASE,
)
# ── IGNORECASE gotcha (cost me a debugging round; worth knowing) ──────────────
# The uppercase-start check MUST be written  (?=(?-i:[A-Z0-9]))  and NOT
# (?=[^a-z]) or (?=[A-Z]).  Under re.IGNORECASE, the class [a-z] also matches
# A-Z, so [^a-z] excludes UPPERCASE too — and the assertion rejects the very
# headings it is meant to accept ("GuardAPI and REST API commands" → no match).
# The scoped inline flag (?-i: … ) turns IGNORECASE off for just that class.


# ══════════════════════════════════════════════════════════════════════════════
# 1b. SNAKE_COMMAND — `<cmd> <snake_case_subcommand> [one arg]`
#
#     Catches the two shapes CLI_INVOCATION's "≥2 assignments" rule misses:
#       • one top-level arg whose value hides a nested '=' inside quotes:
#           grdapi add_custom_property_to_datasource_by_name customProps="A=B"
#       • no args at all:
#           grdapi get_quick_search_info
#
#     The generic signal is the SNAKE_CASE SUB-COMMAND (≥2 underscores) — an
#     identifier shape that is ubiquitous in CLI/API references and vanishingly
#     rare in running prose. Works identically for `az storage_account_create`,
#     `gh repo_create`, etc. No product noun involved.
#
#     Anchored to end-of-line (or to an assignment), so a prose sentence that
#     *mentions* a command ("run the get_quick_search_info command to…") does not
#     match — the trailing words break the anchor.
# ══════════════════════════════════════════════════════════════════════════════
SNAKE_COMMAND = re.compile(
    r"""
    ^[ \t]*
    [a-z][\w.\-]*                       # command token   (grdapi / az / gh)
    \s+
    [a-z][a-z0-9]*(?:_[a-z0-9]+){2,}    # snake_case sub-command, ≥2 underscores
    (?:
        \s*$                            #   …and nothing else            (bare)
      | \s+[\w.\-]+\s*=\s*\S            #   …or followed by an argument  (1+ args)
    )
    """,
    re.VERBOSE,
)


# ── Convenience: is this ONE line reference-ish? ──────────────────────────────

_LINE_PATTERNS = (CLI_INVOCATION, REST_CALL, SYNTAX_TEMPLATE, SNAKE_COMMAND)


def is_command_line(line: str) -> bool:
    """True if the line is an actual command/REST invocation or a syntax template."""
    return any(p.search(line) for p in _LINE_PATTERNS)


def is_reference_scaffolding(line: str) -> bool:
    """True if the line is reference *structure* (syntax/param headings)."""
    return bool(SYNTAX_SECTION.match(line) or PARAM_TABLE_HEADER.match(line))


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER-LEVEL STRIP — the generic replacement for "delete pages 1064–1764".
#
# Page numbers are the least portable thing imaginable: they change with every
# release and mean nothing in another manual. Instead:
#
#   1. Find a REFERENCE_CHAPTER_HEADING  ("GuardAPI and REST API commands").
#   2. From there, walk forward while the content KEEPS LOOKING like reference
#      material — measured on a rolling window of command lines + scaffolding.
#   3. Stop as soon as a sustained run of ordinary prose returns (i.e. the next
#      real chapter), and resume keeping text.
#
# This finds the chapter by SHAPE, so it works on any manual, at any version,
# with any product's command name.
# ══════════════════════════════════════════════════════════════════════════════

def _is_reference_ish(line: str) -> bool:
    return is_command_line(line) or is_reference_scaffolding(line) or bool(ENTRY_HEADING.match(line))


def strip_reference_chapters(
    text: str,
    *,
    window: int = 40,
    enter_window: int = 400,
    enter_density: float = 0.10,
    exit_density: float = 0.05,
    exit_run: int = 60,
) -> tuple[str, dict]:
    """
    Remove entire command/API-reference chapters from *text*.

    Returns ``(cleaned_text, stats)``.

    window        rolling window (lines) used to measure reference-density
    enter_window  how far to look ahead when deciding to ENTER a chapter. Must be
                  LARGE: reference chapters open with several paragraphs of ordinary
                  prose ("GuardAPI commands provide access to…") before the first
                  command entry. A small window measures 0.00 density there and never
                  enters — the exact bug that let the main GuardAPI chapter survive.
    enter_density reference-density required within enter_window to commit to
                  dropping the chapter (guards against a passing prose mention)
    exit_density  once inside, density below this for *exit_run* consecutive
                  lines means the reference chapter has ended
    exit_run      how many sustained prose lines are needed to leave
    """
    lines = text.splitlines()
    n = len(lines)
    keep = [True] * n
    stats = {"chapters_dropped": 0, "lines_dropped": 0, "chapter_titles": []}

    i = 0
    while i < n:
        # A chapter heading must NOT itself be entry-level scaffolding.
        # "REST API syntax" matches REFERENCE_CHAPTER_HEADING, but it is the
        # per-command section heading that appears inside EVERY entry — treating
        # it as a chapter boundary made the stripper re-enter hundreds of times
        # and chew through ordinary prose (23% of the doc, incl. real content).
        if REFERENCE_CHAPTER_HEADING.match(lines[i]) and not is_reference_scaffolding(lines[i]):
            # Look ahead: does reference-like content actually follow?
            look = lines[i + 1 : i + 1 + enter_window]
            dens = (sum(1 for l in look if _is_reference_ish(l)) / len(look)) if look else 0.0
            if dens >= enter_density:
                start = i
                j = i + 1
                prose_run = 0
                while j < n:
                    if _is_reference_ish(lines[j]):
                        prose_run = 0
                    elif lines[j].strip():
                        prose_run += 1
                        if prose_run >= exit_run:
                            # Check the trailing window really is prose before leaving
                            w = lines[max(j - window, 0) : j]
                            d = (sum(1 for l in w if _is_reference_ish(l)) / len(w)) if w else 0.0
                            if d <= exit_density:
                                break
                    j += 1
                for k in range(start, j):
                    if keep[k]:
                        keep[k] = False
                        if lines[k].strip():
                            stats["lines_dropped"] += 1
                stats["chapters_dropped"] += 1
                stats["chapter_titles"].append(lines[start].strip()[:70])
                i = j
                continue
        i += 1

    cleaned = "\n".join(l for l, k in zip(lines, keep) if k)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned, stats


__all__ = [
    "CLI_INVOCATION", "SNAKE_COMMAND", "REST_CALL", "SYNTAX_TEMPLATE", "SYNTAX_SECTION",
    "PARAM_TABLE_HEADER", "ENTRY_HEADING", "REFERENCE_CHAPTER_HEADING",
    "is_command_line", "is_reference_scaffolding", "strip_reference_chapters",
]


# ── Reference HEADINGS (used to prune whole sections from the heading tree) ───
#
# A command/API reference chapter labels its parts with scaffolding headings:
#     "GuardAPI syntax"   "REST API syntax"   "GuardAPI example"
#     "REST API example"  "CLI syntax"        "Command reference"
# Any section sitting under such a heading is reference material, not prose, and
# is exactly what requirement 7 says to remove.
#
# Shape-based and product-agnostic: it keys on "<interface-ish word> +
# syntax|example|reference", never on a vendor name. It therefore prunes
# "GuardAPI example" and "REST API syntax" alike, and would prune
# "StripeAPI example" in another manual.
REFERENCE_HEADING = re.compile(
    r"""
    ^\s*
    (?:
        [\w\-]*                       # optional vendor-ish prefix (Guard/REST/CLI/…)
        \s*
        (?:api|apis|cli|rest|sdk)?    # optional interface word
        \s*
        (?:syntax|example|examples|reference|commands?)   # the scaffolding noun
      | (?:command|api)\s+reference
    )
    \s*$
    """,
    re.VERBOSE | re.IGNORECASE,
)


def is_reference_heading(title: str) -> bool:
    """True when a heading labels command/API reference scaffolding."""
    t = (title or "").strip()
    if not t or len(t) > 40:
        return False
    if not REFERENCE_HEADING.match(t):
        return False
    # Must actually mention an interface, else a plain "Example" heading would be
    # pruned. NOTE the missing leading \b: in "GuardAPI" the API is glued to the
    # vendor prefix, so \bapi\b never matches. Anchoring only the TRAILING
    # boundary catches GuardAPI / StripeAPI / RestAPI as well as a standalone API.
    return bool(re.search(r"(?:api|apis|cli|rest|sdk|commands?)\b", t, re.I))
