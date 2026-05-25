from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import pickle

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

with open("app/model/HPmodel.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={"request": request}
    )
@app.post("/predict")
async def predict(
    area: float = Form(...),
    bedrooms: int = Form(...),
    bathrooms: int = Form(...),
    stories: int = Form(...)
):
    features = np.array([[area, bedrooms, bathrooms, stories]])

    prediction = model.predict(features)

    return {
        "predicted_price": round(prediction[0], 2)
    }