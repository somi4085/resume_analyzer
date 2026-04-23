from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text is not None:
            text += page_text + " "

    return text.strip()