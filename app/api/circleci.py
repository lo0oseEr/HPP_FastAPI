from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")


@router.post("/pipeline")
def trigger_pipeline():

    url = f"https://circleci.com/api/v2/project/{PROJECT_SLUG}/pipeline"

    headers = {
        "Circle-Token": TOKEN,
        "Content-Type": "application/json"
    }

    # Optional request body
    payload = {
        "branch": "main"
    }

    response = requests.post(url, headers=headers, json=payload
    )

    return response.json()