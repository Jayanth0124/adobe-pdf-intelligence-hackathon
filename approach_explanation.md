### Round 1B: Approach Explanation

We designed a lightweight persona-based PDF intelligence engine that works offline without large ML models.

1. **Text Extraction**:
   - Uses PyMuPDF to extract headings and paragraph blocks from each page.

2. **Relevance Scoring**:
   - Simple rule-based keyword matching using tokens from persona and job definition.
   - Headings and body text scored separately.
   - Sorted by relevance and top-ranked entries selected.

3. **Advantages**:
   - Fast, lightweight, no external dependencies.
   - Fully Dockerized for CPU-based execution.
   - Can be extended later with embedding models if allowed.

This system helps users focus on only the sections that matter to them in a sea of content.