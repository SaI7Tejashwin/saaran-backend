from fastapi import APIRouter

router = APIRouter(
    prefix="/predict/abstract",
    tags = ["abstract"],
    responses = {404: {'description': "Not found"}}
)

@router.get("/")
def get_extactive():
    return {"model_type": "abstractive"}