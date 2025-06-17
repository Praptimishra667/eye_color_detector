from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

# Load and prepare data
df = pd.read_csv("synthetic_eye_color_dataset.csv")

snp_columns = df.columns[:-1]
label_encoders = {}

for col in snp_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

target_encoder = LabelEncoder()
df["eye_color_encoded"] = target_encoder.fit_transform(df["eye_color"])

X = df[snp_columns]
y = df["eye_color_encoded"]

model = RandomForestClassifier()
model.fit(X, y)

# Input format
class SNPInput(BaseModel):
    features: list

@app.get("/")
def root():
    return {"message": "API is live!"}

@app.post("/predict")
def predict_snp(input: SNPInput):
    pred = model.predict([input.features])[0]
    decoded = target_encoder.inverse_transform([pred])[0]
    return {"predicted_eye_color": decoded}
