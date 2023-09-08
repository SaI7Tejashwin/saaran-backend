from typing import Annotated
import uvicorn

from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from .predictions import extractive, abstractive
from .predictions.utils.file_extract import extract_file_content

app = FastAPI()

app.include_router(extractive.router)
app.include_router(abstractive.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
class ModelType(str, Enum):
    extract = "extract"
    abstract = "abstract"


# @app.post("/predict/{model_type}")
# async def predict(model_type: ModelType):
#     if model_type is ModelType.extract:
#         return {"model_type": model_type}
    
#     elif model_type is ModelType.abstract:
#         return {"model_type": model_type}
#     else:
#         raise HTTPException(
#             status=403, detail="Invalid model_type"
#         )


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload")
async def get_file_upload(file: UploadFile = File(...)):
    # data = await request.json()
    contents = await file.read()

    filename = file.filename
    extention = file.filename.split(".")[-1]

    # contents = extract_file_content(file)
    return {
            "filename": filename,
            "extention": extention,
            "content": contents
            }

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
