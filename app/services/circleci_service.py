import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("CIRCLECI_TOKEN")

PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")

HEADERS = {
    "Circle-Token": TOKEN
}


def get_pipelines():

    url = f"https://circleci.com/api/v2/project/{PROJECT_SLUG}/pipeline"

    response = requests.get(url, headers=HEADERS)

    return response.json()