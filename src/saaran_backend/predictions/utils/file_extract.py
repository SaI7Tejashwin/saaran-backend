import io

from fastapi import File, UploadFile
from pypdf import PdfReader

async def extract_file_content(file: UploadFile = File(...), extention: str = ""):
    #TODO: text extraction post processing
    if extention == "pdf":
        reader = PdfReader(file.file)
        content = []
        # page = reader.pages[0]
        # print(page.extract_text())
        for page in reader.pages:
            text_body = page.extract_text()
            content.append(text_body.strip())
        # parts = []
        return "".join(content)
    elif extention == "txt":
        content = await file.read()
        return content

def text_post_processing(text_content):
    return