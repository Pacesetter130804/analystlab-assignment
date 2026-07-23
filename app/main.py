import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="AnalystLab Production Prediction API",
    description="API for serving real-time machine learning predictions.",
    version="1.0.0"
)

# Resolve path relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.joblib")

class ModelInput(BaseModel):
    feature_1: float = Field(..., description="First feature value", json_schema_extra={"example": 5.1})
    feature_2: float = Field(..., description="Second feature value", json_schema_extra={"example": 3.5})
    feature_3: float = Field(..., description="Third feature value", json_schema_extra={"example": 1.4})

@app.get("/")
def read_root():
    return {"status": "online", "message": "API active. Visit /docs for documentation."}

@app.post("/predict")
def predict(payload: ModelInput):
    if not os.path.exists(MODEL_PATH):
        raise HTTPException(
            status_code=404, 
            detail=f"Model file not found at path: {MODEL_PATH}"
        )

    try:
        model = joblib.load(MODEL_PATH)
        input_data = np.array([[payload.feature_1, payload.feature_2, payload.feature_3]])
        prediction = model.predict(input_data)

        return {
            "status": "success", 
            "prediction": int(prediction[0])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
