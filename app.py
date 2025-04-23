#Step 2: Create a Simple API (app.py)



# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Define request schema
class IrisFeatures(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: IrisFeatures):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}