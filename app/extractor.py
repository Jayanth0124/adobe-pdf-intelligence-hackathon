import os
import fitz  
import json
from app.utils import clean_text, guess_heading_level

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b['type'] != 0:
                continue
            for line in b["lines"]:
                text = " ".join(span["text"] for span in line["spans"]).strip()
                if not text:
                    continue
                level = guess_heading_level(line["spans"])
                if level:
                    outline.append({
                        "level": level,
                        "text": clean_text(text),
                        "page": page_num
                    })

    return {
        "title": title,
        "outline": outline
    }
