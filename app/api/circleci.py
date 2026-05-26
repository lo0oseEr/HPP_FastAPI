from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")


@router.get("/jobs/{job_number}/tests")
def get_job_artifacts(job_number: int):

    url = f"https://circleci.com/api/v2/project/{PROJECT_SLUG}/{job_number}/tests"

    headers = {
        "Circle-Token": TOKEN,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    print("STATUS CODE:", response.status_code)
    print("RAW RESPONSE:", response.text)

    try:
        data = response.json()
        return data

    except Exception as e:

        return {
            "error": str(e),
            "status_code": response.status_code,
            "raw_response": response.text
        }