import os
import fitz  # PyMuPDF
import json
from datetime import datetime
from app.utils import clean_text, guess_heading_level, match_persona_relevance

def extract_relevant_sections(doc_paths, persona, job):
    extracted_sections = []
    sub_section_analysis = []

    for doc_path in doc_paths:
        doc = fitz.open(doc_path)
        doc_name = os.path.basename(doc_path)

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
                        score = match_persona_relevance(text, persona, job)
                        if score > 0:
                            extracted_sections.append({
                                "document": doc_name,
                                "page": page_num,
                                "section_title": clean_text(text),
                                "importance_rank": score
                            })
                    elif len(text.split()) > 6:
                        score = match_persona_relevance(text, persona, job)
                        if score > 0:
                            sub_section_analysis.append({
                                "document": doc_name,
                                "page": page_num,
                                "refined_text": clean_text(text),
                                "importance_rank": score
                            })

    extracted_sections = sorted(extracted_sections, key=lambda x: x["importance_rank"], reverse=True)[:10]
    sub_section_analysis = sorted(sub_section_analysis, key=lambda x: x["importance_rank"], reverse=True)[:10]

    return {
        "metadata": {
            "documents": [os.path.basename(p) for p in doc_paths],
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_section_analysis
    }