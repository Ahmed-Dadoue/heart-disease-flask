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
TRANSLATIONS = {
    "en": {
        "direction": "ltr",
        "page_title": "Heart Disease Prediction",
        "heading": "Heart Disease Prediction",
        "language_en": "English",
        "language_de": "Deutsch",
        "language_ar": "Arabic",
        "age": "Age",
        "sex": "Sex",
        "cp": "Chest Pain Type",
        "trestbps": "Resting BP",
        "chol": "Cholesterol",
        "fbs": "FBS",
        "restecg": "Rest ECG",
        "thalach": "Max Heart Rate",
        "exang": "Exercise Angina",
        "oldpeak": "Oldpeak",
        "slope": "Slope",
        "ca": "CA",
        "thal": "Thal",
        "predict_button": "Predict",
        "result_label": "Result",
        "probability_label": "Risk Probability",
        "high_risk": "High Risk of Heart Disease",
        "low_risk": "Low Risk",
    },
    "de": {
        "direction": "ltr",
        "page_title": "Herzerkrankungs-Prognose",
        "heading": "Herzerkrankungs-Prognose",
        "language_en": "English",
        "language_de": "Deutsch",
        "language_ar": "Arabisch",
        "age": "Alter",
        "sex": "Geschlecht",
        "cp": "Brustschmerztyp",
        "trestbps": "Ruheblutdruck",
        "chol": "Cholesterin",
        "fbs": "Nuechternblutzucker",
        "restecg": "Ruhe-EKG",
        "thalach": "Max Herzfrequenz",
        "exang": "Belastungsangina",
        "oldpeak": "Oldpeak",
        "slope": "Steigung",
        "ca": "CA",
        "thal": "Thal",
        "predict_button": "Vorhersagen",
        "result_label": "Ergebnis",
        "probability_label": "Risikowahrscheinlichkeit",
        "high_risk": "Hohes Risiko fuer Herzerkrankung",
        "low_risk": "Niedriges Risiko",
    },
    "ar": {
        "direction": "rtl",
        "page_title": "التنبؤ بأمراض القلب",
        "heading": "التنبؤ بأمراض القلب",
        "language_en": "الإنجليزية",
        "language_de": "الألمانية",
        "language_ar": "العربية",
        "age": "العمر",
        "sex": "الجنس",
        "cp": "نوع ألم الصدر",
        "trestbps": "ضغط الدم أثناء الراحة",
        "chol": "الكوليسترول",
        "fbs": "سكر الدم الصائم",
        "restecg": "تخطيط القلب أثناء الراحة",
        "thalach": "أقصى معدل لنبض القلب",
        "exang": "ذبحة صدرية مع المجهود",
        "oldpeak": "الانخفاض ST",
        "slope": "الميل",
        "ca": "عدد الأوعية",
        "thal": "الثال",
        "predict_button": "توقع النتيجة",
        "result_label": "النتيجة",
        "probability_label": "احتمال الخطورة",
        "high_risk": "خطر مرتفع للإصابة بمرض القلب",
        "low_risk": "خطر منخفض",
    },
}

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)
model = joblib.load(MODEL_PATH)


def get_language(value):
    return value if value in TRANSLATIONS else "en"


@app.route("/")
def home():
    lang = get_language(request.args.get("lang", "en"))
    return render_template(
        "index.html",
        prediction=None,
        probability=None,
        lang=lang,
        text=TRANSLATIONS[lang],
    )


@app.route("/predict", methods=["POST"])
def predict():
    lang = get_language(request.form.get("lang", "en"))
    text = TRANSLATIONS[lang]
    features = {field: float(request.form[field]) for field in FEATURE_FIELDS}
    df = pd.DataFrame([features], columns=FEATURE_FIELDS)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    if prediction == 1:
        result = text["high_risk"]
    else:
        result = text["low_risk"]

    return render_template(
        "index.html",
        prediction=result,
        probability=round(probability * 100, 2),
        lang=lang,
        text=text,
    )


if __name__ == "__main__":
    app.run(debug=True)
