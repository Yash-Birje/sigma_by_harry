from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
class InputData(BaseModel):
    x1: float
    x2: float


with open("./weights/weights_LinearRegression.json", "r") as f:
    data = json.load(f)

weights = data["weights"]
bias = data["bias"]

print(weights)  # list
print(bias)     # float

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    w,b = weights, bias
    model = w[0][0] * float(data.x1) + w[1][0] * float(data.x2) + b
    return {"prediction": model}