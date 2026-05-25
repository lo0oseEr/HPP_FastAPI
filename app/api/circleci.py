from fastapi import APIRouter

router = APIRouter()

@router.get("/pipelines")
def get_pipelines():
    return {
        "message": "CircleCI pipeline working"
    }