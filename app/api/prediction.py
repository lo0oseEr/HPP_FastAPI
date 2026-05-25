import traceback
import pandas as pd

@app.post("/predict")
async def predict(
    area: float = Form(...),
    bedrooms: int = Form(...),
    bathrooms: int = Form(...),
    stories: int = Form(...)
):
    try:

        features = pd.DataFrame({
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "stories": [stories]
        })

        prediction = model.predict(features)

        return {
            "predicted_price": round(float(prediction[0]), 2)
        }

    except Exception as e:
        traceback.print_exc()

        return {
            "error": str(e)
        }