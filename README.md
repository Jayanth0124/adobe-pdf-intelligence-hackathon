# 🧠 Adobe India Hackathon – “Connecting the Dots” Challenge

## 🚀 Project: Intelligent PDF Processor (Round 1A + Round 1B)

This project reimagines the humble PDF as an intelligent, interactive experience. It extracts structured outlines, understands document semantics, and surfaces relevant insights based on user personas — all powered by a single Dockerized system.

---

## 🔹 Round 1A – Extracting Structured Outlines from PDFs

### 🎯 Objective:
Given a PDF, extract:
- The **document title**
- Headings (`H1`, `H2`, `H3`) with their page numbers
- Output a structured JSON outline

### 📥 Input:
- A single PDF (≤ 50 pages)

### 📤 Output (sample format):
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

### 💡 Why It Matters:
PDFs are visually structured for humans but not for machines. This round builds the foundation for intelligent document understanding like semantic search and recommendation engines.

---

## 🔹 Round 1B – Persona-Based Document Intelligence

### 🎯 Objective:
Extract and rank the **most relevant sections and sub-sections** from a collection of PDFs based on a given **persona** and their **job-to-be-done**.

### 📥 Input:
- A set of 3–10 PDF documents
- Persona description (e.g., “PhD Researcher in Computational Biology”)
- Job-to-be-done (e.g., “Prepare a literature review on GNNs for drug discovery”)

### 📤 Output (sample format):
```json
{
  "metadata": {
    "documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Literature review on GNNs for drug discovery",
    "timestamp": "2025-07-16T12:00:00"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "section_title": "GNN for Molecule Prediction",
      "importance_rank": 6
    }
  ],
  "sub_section_analysis": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "refined_text": "GNN models are effective for predicting molecular properties...",
      "importance_rank": 5
    }
  ]
}
```

### 💡 Why It Matters:
This simulates real-world research and review use cases by tailoring output to the user’s goal.

---

## 🧰 Tech Stack

- Python 3.9
- PyMuPDF
- Docker (CPU-only, no internet required)
- Linux/amd64 image (no GPU)

---

## 🏗️ Folder Structure

```
project-root/
├── app/
│   ├── extractor.py
│   ├── persona_extractor.py
│   ├── run.py
│   ├── run_b.py
│   ├── utils.py
│   └── __init__.py
├── input/             # PDF input files
├── output/            # Extracted JSON files
├── run.sh             # Unified script for Round 1A and 1B
├── Dockerfile
├── requirements.txt
├── README.md
└── approach_explanation.md
```

---

## 🧪 How to Build & Run

### 🛠️ Build Docker Image:

```bash
docker build --platform linux/amd64 -t pdfextractor:multi .
```

### ▶️ Run Round 1A:

```bash
docker run --rm -e MODE=1A ^
 -v "<absolute_path>/input:/app/input" ^
 -v "<absolute_path>/output:/app/output" ^
 --network none pdfextractor:multi
```

### ▶️ Run Round 1B:

```bash
docker run --rm -e MODE=1B ^
 -v "<absolute_path>/input:/app/input" ^
 -v "<absolute_path>/output:/app/output" ^
 --network none pdfextractor:multi
```

---

## 📝 Submission Notes

- All requirements met (offline, ≤10s for Round 1A, ≤60s for Round 1B, CPU-only)
- Repo contains Dockerfile, scripts, explanation docs, and working code
- Persona and job can be customized in `run_b.py`