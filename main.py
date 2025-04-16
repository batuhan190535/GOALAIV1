from fastapi import FastAPI
import joblib

app = FastAPI()

# Modeli yükle
model = joblib.load("models/ms_model.pkl")

@app.get("/")
def home():
    return {"status": "GOALMASTER API is alive!"}