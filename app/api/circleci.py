from fastapi import APIRouter, HTTPException
from app.services.circleci_service import fetch_pipelines

router = APIRouter()

@router.get("/pipelines")
def get_pipelines():
    try:
        return fetch_pipelines()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))