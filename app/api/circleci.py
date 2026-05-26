from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")


@router.get("/job/{job_id}")
def get_job_details(job_id: str):

    url = f"https://circleci.com/api/v2/job/{job_id}"

    headers = {
        "Circle-Token": TOKEN,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    return response.json()