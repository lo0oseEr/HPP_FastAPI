from fastapi import APIRouter
from app.services.circleci_service import get_pipelines

router = APIRouter()


@router.get("/pipelines")
def pipelines():

    return get_pipelines()