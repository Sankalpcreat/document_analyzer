import pdfplumber
import os

def parse_pdf(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with pdfplumber.open(file_path) as pdf:
            text = " ".join(page.extract_text() or "" for page in pdf.pages)
            if not text.strip():
                raise ValueError("PDF file is empty or contains no extractable text")
            return text
    except Exception as e:
        logging.error(f"Error parsing PDF file: {e}")
        return "Error: Unable to parse PDF"