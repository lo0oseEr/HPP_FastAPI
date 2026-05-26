from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")


@router.get("/workflow/{workflow_id}")
def get_workflow_details(workflow_id: str):

    url = f"https://circleci.com/api/v2/workflow/{workflow_id}"

    headers = {
        "Circle-Token": TOKEN,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    return response.json()