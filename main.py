"""Deterministic text windows with recoverable character offsets."""
import argparse
import hashlib
import json
from pathlib import Path
import re


def chunk_text(text, source_id, size=40, overlap=8):
    if not isinstance(source_id, str) or not source_id:
        raise ValueError("source_id must be nonempty")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (size, overlap)) or size <= 0 or not 0 <= overlap < size:
        raise ValueError("require integer size > 0 and 0 <= overlap < size")
    matches = list(re.finditer(r"\S+", text))
    chunks = []
    start = 0
    while start < len(matches):
        end = min(start + size, len(matches))
        char_start, char_end = matches[start].start(), matches[end - 1].end()
        body = text[char_start:char_end]
        digest = hashlib.sha256(f"{source_id}\0{char_start}\0{char_end}\0{body}".encode()).hexdigest()[:16]
        chunks.append({"id": f"{source_id}:{digest}", "source_id": source_id,
                       "token_start": start, "token_end": end, "char_start": char_start,
                       "char_end": char_end, "text": body})
        if end == len(matches):
            break
        start = end - overlap
    return chunks

