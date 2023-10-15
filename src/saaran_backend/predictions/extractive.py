from enum import Enum
from fastapi import APIRouter, BackgroundTasks, File, UploadFile
from pydantic import BaseModel

from .utils.file_extract import extract_file_content

#util ML functions
from .utils.sumy import (
    sumy_kl_summarize,
    sumy_lex_summarize,
    sumy_luhn_summarize,
    sumy_lsa_summarize
    )

router = APIRouter(
    prefix="/predict/extract",
    tags = ["extract"],
    responses = {404: {'description': "Not found"}}
)

'''
Need to define a input body such as 
{
    file: ...., //probably base-64 encoded
    sentences: ...,
    extention: ... #To handle the file-types
}
'''

class SumyModelName(str, Enum):
    sumy_lex = "sumy_lex"
    sumy_luhn = "sumy_luhn"
    sumy_kl = "sumy_kl"
    sumy_lsa = "sumy_lsa"


@router.get("/")
def get_extactive():
    return {"model_type": "extractive"}

@router.post('/{sumy_model_name}')
async def predict_sumy(sumy_model_name: SumyModelName ,file: UploadFile = File(...)):

    f_extention: str = file.filename.split(".")[-1]
    if f_extention == "pdf":
        f_content: str = await extract_file_content(file)
    elif f_extention == "docx" or f_extention == "txt":
        f_content: str = await file.read()
    summary: str = None
    if sumy_model_name is SumyModelName.sumy_lex:
        summary = sumy_lex_summarize(f_content)
    elif sumy_model_name is SumyModelName.sumy_luhn:
        summary = sumy_luhn_summarize(f_content)
    elif sumy_model_name is SumyModelName.sumy_kl:
        summary = sumy_kl_summarize(f_content)
    elif sumy_model_name is SumyModelName.sumy_lsa:
        summary = sumy_lsa_summarize(f_content)

    return {"extention": f_extention, "summary": summary, "message": "text summarized"} if summary else {"message": "not summarized"}  


