from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import models.LinearRegression as lr

class InputData(BaseModel):
    x1: float
    x2: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    model = lr.w[0]*data.x1 + lr.w[1]*data.x2 + lr.b
    return {"prediction": model.item()}