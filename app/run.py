import sys
from app.extractor import extract_outline
import json

def main():
    input_pdf = sys.argv[1]
    output_json = sys.argv[2]

    result = extract_outline(input_pdf)
    with open(output_json, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()