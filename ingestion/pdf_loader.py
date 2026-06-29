from pdfminer.high_level import extract_text

def load_pdf(pdf_path):

    text = extract_text(pdf_path)
    if not text or not text.strip():
        raise Exception(
            "No extractable text found in PDF"
        )

    return text