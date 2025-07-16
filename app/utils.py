import unicodedata
import re

def clean_text(text):
    return " ".join(text.strip().split())

def guess_heading_level(spans):
    if not spans:
        return None

    font_size = spans[0]["size"]
    text = spans[0]["text"].strip()

    # Normalize unicode and check if it's only digits or punctuation
    cleaned = unicodedata.normalize("NFKC", text)
    if not re.search(r'\w', cleaned, flags=re.UNICODE):
        return None
    if len(cleaned) < 2:
        return None
    if cleaned.lower().startswith("http") or cleaned.isdigit():
        return None

    if font_size > 16:
        return "H1"
    elif font_size > 13:
        return "H2"
    elif font_size > 11:
        return "H3"
    return None

def match_persona_relevance(text, persona, job):
    # Simple multilingual token overlap (works across English, Japanese, Hindi, etc.)
    keywords = (persona + " " + job).lower().split()
    text_lower = text.lower()
    matches = sum(1 for word in keywords if word in text_lower)
    return matches