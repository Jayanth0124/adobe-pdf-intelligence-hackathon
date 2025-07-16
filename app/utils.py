def clean_text(text):
    return " ".join(text.strip().split())

def guess_heading_level(spans):
    if not spans:
        return None
    font_size = spans[0]["size"]
    if font_size > 16:
        return "H1"
    elif font_size > 13:
        return "H2"
    elif font_size > 11:
        return "H3"
    return None