import re

def clean_text(text):
    text = text.lower()

    # FIXED REGEX
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    text = re.sub(r'\s+', ' ', text).strip()

    return text
