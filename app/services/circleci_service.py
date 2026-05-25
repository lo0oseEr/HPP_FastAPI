import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("CIRCLECI_TOKEN")
PROJECT_SLUG = os.getenv("CIRCLECI_PROJECT_SLUG")

headers = {
    "Circle-Token": TOKEN
}

def fetch_pipelines():
    url = f"https://circleci.com/api/v2/project/{PROJECT_SLUG}/pipeline"

    response = requests.get(url, headers=headers)

    return response.json()