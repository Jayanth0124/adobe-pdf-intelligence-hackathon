# Adobe India Hackathon - PDF Outline Extractor (Round 1A)

## 🎯 Objective
Extract structured outline (Title, H1, H2, H3) from PDFs.

---

## 🏗️ Tech Stack
- Python 3.9
- PyMuPDF (fitz)
- Docker (linux/amd64)

---

## 📁 Input/Output

- Input: PDF files in `/app/input/`
- Output: JSON files in `/app/output/`

---

## ⚙️ How to Run (Docker)

```bash
docker build --platform linux/amd64 -t pdfextractor:demo .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdfextractor:demo
```

---

## 📦 Output Format

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

---

## ✅ Constraints Met
- ⏱️ ≤ 10s runtime
- 🧠 ≤ 200MB (no model)
- ❌ No internet
- ✅ CPU-only