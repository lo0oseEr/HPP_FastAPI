from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.prediction import router as prediction_router
from app.api.circleci import router as circleci_router

# Create FastAPI app FIRST
app = FastAPI()

# Templates
templates = Jinja2Templates(directory="app/templates")


# Home Route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Include Prediction API
app.include_router(prediction_router)

# Include CircleCI API
app.include_router(circleci_router)