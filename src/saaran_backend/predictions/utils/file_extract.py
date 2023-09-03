from fastapi import File, UploadFile
from pypdf import PdfReader

def extract_file_content(file: UploadFile = File(...)):
    #TODO: text extraction post processing
    reader = PdfReader(file.file)
    page = reader.pages[0]
    # print(page.extract_text())

    return page.extract_text()