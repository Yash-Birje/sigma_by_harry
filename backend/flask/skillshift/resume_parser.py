from PyPDF2 import PdfReader
from docx import Document
import os
import re

def extract_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text_chunks = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_chunks.append(page_text)

    return "\n".join(text_chunks)

def extract_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    text_chunks = []

    for para in doc.paragraphs:
        if para.text.strip():
            text_chunks.append(para.text)

    return "\n".join(text_chunks)

def extract_resume_text(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found")

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".pdf":
        raw_text = extract_from_pdf(file_path)
    elif ext == ".docx":
        raw_text = extract_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")

    # light cleanup
    raw_text = re.sub(r"\s+", " ", raw_text)
    return raw_text.strip()
