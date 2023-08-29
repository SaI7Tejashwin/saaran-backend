from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel

#util ML functions
from .extractive_utils.sumy import sumy_lex_summarize

router = APIRouter(
    prefix="/predict/extract",
    tags = ["extract"],
    responses = {404: {'description': "Not found"}}
)

class InputText(BaseModel):
    text: str

@router.get("/")
def get_extactive():
    return {"model_type": "extractive"}

@router.post('/sumy')
async def predict_sumy(input_text: InputText, background_tasks: BackgroundTasks):
    summary = sumy_lex_summarize(input_text)
    return {"summary": summary, "message": "text summarized"}