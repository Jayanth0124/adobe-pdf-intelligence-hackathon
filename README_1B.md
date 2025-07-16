# Adobe Hackathon - Round 1B: Persona-Based PDF Intelligence

## 🧠 Goal
Given multiple PDFs, a persona, and a job-to-be-done, extract and rank the most relevant sections and paragraphs.

---

## 🏗️ Tech Stack
- Python 3.9
- PyMuPDF (fitz)
- Docker (linux/amd64)

---

## 🚀 How to Run (Docker)

```bash
docker build --platform linux/amd64 -t personaextractor:round1b .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none personaextractor:round1b
```

---

## 📄 Output Format
A JSON file `persona_output.json` with:
- Metadata
- Ranked sections
- Ranked sub-sections

---

## ✅ Constraints Met
- CPU-only
- No internet
- ≤ 60s runtime
- ≤ 1GB size