from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "pipeline.joblib"
FEATURE_FIELDS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)
model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html", prediction=None, probability=None)


@app.route("/predict", methods=["POST"])
def predict():
    features = {field: float(request.form[field]) for field in FEATURE_FIELDS}
    df = pd.DataFrame([features], columns=FEATURE_FIELDS)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    if prediction == 1:
        result = "⚠ High Risk of Heart Disease"
    else:
        result = "✅ Low Risk"

    return render_template(
        "index.html",
        prediction=result,
        probability=round(probability * 100, 2),
    )


if __name__ == "__main__":
    app.run(debug=True)
