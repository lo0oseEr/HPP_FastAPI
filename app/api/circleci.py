from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")


@router.get("/pipeline/{pipeline_id}/workflow")
def get_pipeline_config(pipeline_id: str):

    url = f"https://circleci.com/api/v2/pipeline/{pipeline_id}/workflow"

    headers = {
        "Circle-Token": TOKEN,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    return response.json()