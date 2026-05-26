from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")


@router.get("/pipeline/{pipeline_number}")
def get_pipeline_by_number(pipeline_number: int):

    headers = {
        "Circle-Token": TOKEN,
        "Accept": "application/json"
    }

    # Fetch pipeline list
    url = f"https://circleci.com/api/v2/project/{PROJECT_SLUG}/pipeline"

    response = requests.get(url, headers=headers)

    data = response.json()

    # Match pipeline number
    for item in data.get("items", []):

        if item.get("number") == pipeline_number:

            return {
                "pipeline_number": item.get("number"),
                "pipeline_id": item.get("id"),
                "state": item.get("state"),
                "branch": item.get("vcs", {}).get("branch"),
                "created_at": item.get("created_at")
            }

    return {"message": "Pipeline not found"}