#!/usr/bin/env python3
"""
test_query/serve.py
───────────────────
Tiny static file server that serves ui.html at http://localhost:8089/ui.html

Why this exists
───────────────
Browsers block fetch() calls from file:// pages to http:// servers (mixed
content / file-origin restriction).  Serving the page over http:// — even on
a different port — bypasses this because:
  • http://localhost:8089  →  http://localhost:8088   is a normal cross-origin
    HTTP request, and the FastAPI app already returns Allow-Origin: *.

Usage
─────
    python test_query/serve.py          # serves on port 8089 (default)
    python test_query/serve.py 8090     # custom port

Then open:  http://localhost:8089/ui.html
"""
import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8089
DIR  = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

class _Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):   # suppress per-request noise
        pass
    def end_headers(self):
        # Allow the page to call the FastAPI server cross-origin
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

print(f"UI server →  http://localhost:{PORT}/ui.html")
print("FastAPI   →  http://localhost:8088  (must be running separately)")
print("Press Ctrl+C to stop.\n")

with http.server.HTTPServer(("", PORT), _Handler) as httpd:
    httpd.serve_forever()
