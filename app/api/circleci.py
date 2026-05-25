from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")

@router.get("/pipeline")
def get_pipeline():

    url = f"https://circleci.com/api/v2/project/{PROJECT_SLUG}/pipeline"

    headers = {
        "Circle-Token": TOKEN,
        "Accept": "application/json"
    }

    # Debug prints
    print(PROJECT_SLUG)
    print(TOKEN)
    print(url)

    response = requests.get(url, headers=headers)

    return response.json()

