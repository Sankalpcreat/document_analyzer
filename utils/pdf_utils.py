import pdfplumber

def parse_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return " ".join(page.extract_text() for page in pdf.pages if page.extract_text())