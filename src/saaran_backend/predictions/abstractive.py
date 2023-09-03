from enum import Enum
from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from .utils.transformers import summarize_bart, summarize_t5

router = APIRouter(
    prefix="/predict/abstract",
    tags = ["abstract"],
    responses = {404: {'description': "Not found"}}
)

class InputText(BaseModel):
    text: str

class TModelName(str, Enum):
    t5 = "t5"
    bart = "bart"

@router.get("/")
def get_extactive():
    return {"model_type": "abstractive"}

#TODO: handle this later -> not working as intended
# @router.post("/{tmodel_name}")
# async def predict_abstractive_summary(tmodel_name: TModelName, file: UploadFile = File(...)):
#     f_extention: str = file.filename.split(".")[-1]
#     f_name: str = file.filename
#     f_content: str = await file.read()
#     summary: str = None

#     if tmodel_name is TModelName.t5:
#         summary = summarize_t5(f_content)
#         return {"filename": f_name, "extention": f_extention, "summary": summary, "message": "text summarized"}
#     elif tmodel_name is TModelName.bart:
#         summary = summarize_bart(f_content)
#         return {"filename": f_name, "extention": f_extention, "summary": summary, "message": "text summarized"}
    
@router.post("/test")
async def predict_abstract(input_text: InputText):
    summary: str = summarize_bart(input_text.text)

    return { "content" : summary }
