# app/utils/syllabus_parser.py
import re
import json
import os
from pathlib import Path

# choose a PDF reader you have; PyPDF2 is lightweight
try:
    from PyPDF2 import PdfReader
except Exception:
    PdfReader = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(BASE_DIR, "data", "known_topics.json")

SPLIT_TOKENS = [",", ";", " - ", " — ", ":", " / ", " and ", " or "]

def text_from_pdf(path: str) -> str:
    if PdfReader is None:
        raise RuntimeError("PyPDF2 not installed. pip install PyPDF2")
    reader = PdfReader(path)
    pages = []
    for p in reader.pages:
        try:
            pages.append(p.extract_text() or "")
        except Exception:
            pages.append("")
    return "\n".join(pages)

def extract_candidate_phrases(text: str):
    text = text.lower()
    # remove common line noise
    text = re.sub(r"\s+", " ", text)
    candidates = set()

    # heuristics: split on tokens
    parts = [text]
    for tok in SPLIT_TOKENS:
        new = []
        for p in parts:
            new.extend(p.split(tok))
        parts = new

    for p in parts:
        p = p.strip()
        # ignore short words and sentences
        if not p or len(p) < 4:
            continue
        # ignore lines starting with 'unit' or 'syllabus' etc.
        if re.match(r"^(unit|syllabus|course|paper|chapter)\b", p):
            continue
        # take only few-word phrases
        words = p.split()
        if 1 < len(words) <= 6:
            candidates.add(" ".join(words).strip())

    return sorted(candidates)

def generate_known_topics_from_pdf(pdf_path: str, out_path: str = OUT_PATH, limit: int = 400):
    txt = text_from_pdf(pdf_path)
    candidates = extract_candidate_phrases(txt)
    # crude frequency or uniqueness — keep them all and let manual prune later
    candidates = candidates[:limit]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(candidates, fh, indent=2, ensure_ascii=False)
    print("Saved known topics to", out_path)
    return out_path

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python syllabus_parser.py path/to/syllabus.pdf")
    else:
        generate_known_topics_from_pdf(sys.argv[1])
