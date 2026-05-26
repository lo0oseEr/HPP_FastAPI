from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")


@router.get("/job/{job_number}")
def get_job_details(job_number: int):

    url = f"https://circleci.com/api/v2/project/{PROJECT_SLUG}/job/{job_number}"

    headers = {
        "Circle-Token": TOKEN,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    return response.json()