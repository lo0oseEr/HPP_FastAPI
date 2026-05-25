from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.prediction import router as prediction_router
from app.api.circleci import router as circleci_router

app = FastAPI()


templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


app.include_router(prediction_router)

app.include_router(
    circleci_router,
    prefix="/api",
    tags=["CircleCI"]
)

print("API is running on http://localhost:8000")