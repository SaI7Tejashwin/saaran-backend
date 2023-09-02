from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from predictions import extractive, abstractive

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
async def get_file_upload(file: UploadFile):
    # data = await request.json()
    contents = await file.read()
    return {
            "filename": file.filename,
            "extention": file.filename.split(".")[-1],
            "content": contents
            }
