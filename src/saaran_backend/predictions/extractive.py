from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel

#util ML functions
from .extractive_utils.sumy import (
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

class InputText(BaseModel):
    text: str

@router.get("/")
def get_extactive():
    return {"model_type": "extractive"}

@router.post('/sumy-lex')
async def predict_sumy_lex(input_text: InputText, background_tasks: BackgroundTasks):
    summary = sumy_lex_summarize(input_text)
    return {"summary": summary, "message": "text summarized"}

@router.post('/sumy-luhn')
async def predict_sumy(input_text: InputText, background_tasks: BackgroundTasks):
    summary = sumy_luhn_summarize(input_text)
    return {"summary": summary, "message": "text summarized"}

@router.post('/sumy-kl')
async def predict_sumy(input_text: InputText, background_tasks: BackgroundTasks):
    summary = sumy_kl_summarize(input_text)
    return {"summary": summary, "message": "text summarized"}

@router.post('/sumy-lsa')
async def predict_sumy(input_text: InputText, background_tasks: BackgroundTasks):
    summary = sumy_lsa_summarize(input_text)
    return {"summary": summary, "message": "text summarized"}