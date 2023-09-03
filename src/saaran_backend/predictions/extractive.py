from enum import Enum
from fastapi import APIRouter, BackgroundTasks, File, UploadFile
from pydantic import BaseModel

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
    f_content: str = await file.read()
    summary: str = None
    if sumy_model_name is SumyModelName.sumy_lex:
        summary = sumy_lex_summarize(f_content)
        return {"extention": f_extention, "summary": summary, "message": "text summarized"}
    elif sumy_model_name is SumyModelName.sumy_luhn:
        summary = sumy_luhn_summarize(f_content)
        return {"extention": f_extention, "summary": summary, "message": "text summarized"}
    elif sumy_model_name is SumyModelName.sumy_kl:
        summary = sumy_kl_summarize(f_content)
        return {"extention": f_extention, "summary": summary, "message": "text summarized"}
    elif sumy_model_name is SumyModelName.sumy_lsa:
        summary = sumy_lsa_summarize(f_content)
        return {"extention": f_extention, "summary": summary, "message": "text summarized"}       


# @router.post('/sumy-lex')
# async def predict_sumy_lex(input_text: InputText, background_tasks: BackgroundTasks):
#     summary = sumy_lex_summarize(input_text)
#     return {"summary": summary, "message": "text summarized"}

# @router.post('/sumy-luhn')
# async def predict_sumy(input_text: InputText, background_tasks: BackgroundTasks):
#     summary = sumy_luhn_summarize(input_text)
#     return {"summary": summary, "message": "text summarized"}

# @router.post('/sumy-kl')
# async def predict_sumy(input_text: InputText, background_tasks: BackgroundTasks):
#     summary = sumy_kl_summarize(input_text)
#     return {"summary": summary, "message": "text summarized"}

# @router.post('/sumy-lsa')
# async def predict_sumy(input_text: InputText, background_tasks: BackgroundTasks):
#     summary = sumy_lsa_summarize(input_text)
#     return {"summary": summary, "message": "text summarized"}