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

    url = "https://circleci.com/api/v2/project/gh/lo0oseEr/HPP_FastAPI/pipeline"

    response = requests.get(
        url,
        headers=HEADERS
    )

    print(response.status_code)
    print(response.text)

    return response.json()