import sys
import json
import glob
from app.persona_extractor import extract_relevant_sections

def main():
    persona = "PhD Researcher in Computational Biology"
    job = "Literature review on drug discovery with GNNs"
    doc_paths = glob.glob("/app/input/*.pdf")
    output = extract_relevant_sections(doc_paths, persona, job)
    with open("/app/output/persona_output.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()