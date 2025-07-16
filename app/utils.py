def clean_text(text):
    return " ".join(text.strip().split())

def guess_heading_level(spans):
    if not spans:
        return None

    font_size = spans[0]["size"]
    text = spans[0]["text"].strip().lower()

    # Optional filter: Skip short, numeric, or URL-like headings
    if len(text) < 4 or text.startswith("http") or text.isdigit():
        return None

    if font_size > 16:
        return "H1"
    elif font_size > 13:
        return "H2"
    elif font_size > 11:
        return "H3"
    return None

def match_persona_relevance(text, persona, job):
    keywords = (persona + " " + job).lower().split()
    matches = sum(1 for word in keywords if word in text.lower())
    return matches
