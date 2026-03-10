from pathlib import Path

import joblib
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "pipeline.joblib"
TRANSLATIONS = {
    "en": {
        "direction": "ltr",
        "page_title": "Heart Disease Prediction",
        "heading": "Heart Disease Prediction",
        "language_en": "English",
        "language_de": "Deutsch",
        "language_ar": "العربية",
        "age": "Age",
        "sex": "Sex",
        "cp": "Chest Pain Type",
        "trestbps": "Resting BP",
        "chol": "Cholesterol",
        "fbs": "Fasting Blood Sugar",
        "restecg": "Resting ECG",
        "thalach": "Max Heart Rate",
        "exang": "Exercise Angina",
        "oldpeak": "Oldpeak",
        "slope": "Slope",
        "ca": "Major Vessels",
        "thal": "Thalassemia",
        "predict_button": "Predict",
        "result_label": "Result",
        "probability_label": "Risk Probability",
        "high_risk": "High Risk of Heart Disease",
        "low_risk": "Low Risk",
        "sex_select": "Choose sex",
        "sex_male": "Male",
        "sex_female": "Female",
        "cp_select": "Choose chest pain type",
        "cp_typical": "Typical Angina",
        "cp_atypical": "Atypical Angina",
        "cp_noanginal": "Non-Anginal Pain",
        "cp_asymp": "Asymptomatic",
        "fbs_select": "Choose fasting blood sugar level",
        "fbs_high": "> 120 mg/dl",
        "fbs_low": "≤ 120 mg/dl",
        "restecg_select": "Choose resting ECG result",
        "restecg_normal": "Normal",
        "restecg_stt": "ST-T Wave Abnormality",
        "restecg_hvh": "Left Ventricular Hypertrophy",
        "exang_select": "Choose",
        "exang_yes": "Yes",
        "exang_no": "No",
        "slope_select": "Choose slope",
        "slope_up": "Upsloping",
        "slope_flat": "Flat",
        "slope_down": "Downsloping",
        "thal_select": "Choose thalassemia type",
        "thal_normal": "Normal",
        "thal_fixed": "Fixed Defect",
        "thal_reversible": "Reversible Defect",
    },
    "de": {
        "direction": "ltr",
        "page_title": "Herzerkrankungs-Prognose",
        "heading": "Herzerkrankungs-Prognose",
        "language_en": "English",
        "language_de": "Deutsch",
        "language_ar": "العربية",
        "age": "Alter",
        "sex": "Geschlecht",
        "cp": "Brustschmerztyp",
        "trestbps": "Ruheblutdruck",
        "chol": "Cholesterin",
        "fbs": "Nüchternblutzucker",
        "restecg": "Ruhe-EKG",
        "thalach": "Max Herzfrequenz",
        "exang": "Belastungsangina",
        "oldpeak": "Oldpeak",
        "slope": "Steigung",
        "ca": "Major Arterien",
        "thal": "Thalassämie",
        "predict_button": "Vorhersagen",
        "result_label": "Ergebnis",
        "probability_label": "Risikowahrscheinlichkeit",
        "high_risk": "Hohes Risiko für Herzerkrankung",
        "low_risk": "Niedriges Risiko",
        "sex_select": "Geschlecht wählen",
        "sex_male": "Männlich",
        "sex_female": "Weiblich",
        "cp_select": "Brustschmerztyp wählen",
        "cp_typical": "Typische Angina",
        "cp_atypical": "Atypische Angina",
        "cp_noanginal": "Nicht-anginöse Schmerzen",
        "cp_asymp": "Asymptomatisch",
        "fbs_select": "Nüchternblutzucker wählen",
        "fbs_high": "> 120 mg/dl",
        "fbs_low": "≤ 120 mg/dl",
        "restecg_select": "Ruhe-EKG-Ergebnis wählen",
        "restecg_normal": "Normal",
        "restecg_stt": "ST-T-Wellen-Anomalie",
        "restecg_hvh": "Linksventrikuläre Hypertrophie",
        "exang_select": "Wählen",
        "exang_yes": "Ja",
        "exang_no": "Nein",
        "slope_select": "Steigung wählen",
        "slope_up": "Ansteigend",
        "slope_flat": "Flach",
        "slope_down": "Absteigend",
        "thal_select": "Thalassämie-Typ wählen",
        "thal_normal": "Normal",
        "thal_fixed": "Festgestellter Defekt",
        "thal_reversible": "Reversibler Defekt",
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
        "ca": "عدد الأوعية الرئيسية",
        "thal": "الثال",
        "predict_button": "توقع النتيجة",
        "result_label": "النتيجة",
        "probability_label": "احتمال الخطورة",
        "high_risk": "خطر مرتفع للإصابة بمرض القلب",
        "low_risk": "خطر منخفض",
        "sex_select": "اختر الجنس",
        "sex_male": "ذكر",
        "sex_female": "أنثى",
        "cp_select": "اختر نوع ألم الصدر",
        "cp_typical": "ذبحة صدرية نموذجية",
        "cp_atypical": "ذبحة صدرية غير نموذجية",
        "cp_noanginal": "ألم غير ذبحي",
        "cp_asymp": "بدون أعراض",
        "fbs_select": "اختر مستوى سكر الدم الصائم",
        "fbs_high": "أكبر من 120 ملغ/ديسيلتر",
        "fbs_low": "120 ملغ/ديسيلتر أو أقل",
        "restecg_select": "اختر نتيجة تخطيط القلب",
        "restecg_normal": "طبيعي",
        "restecg_stt": "اضطراب موجة ST-T",
        "restecg_hvh": "تضخم البطين الأيسر",
        "exang_select": "اختر",
        "exang_yes": "نعم",
        "exang_no": "لا",
        "slope_select": "اختر الميل",
        "slope_up": "صاعد",
        "slope_flat": "مسطح",
        "slope_down": "هابط",
        "thal_select": "اختر نوع الثال",
        "thal_normal": "طبيعي",
        "thal_fixed": "عيب ثابت",
        "thal_reversible": "عيب قابل للعكس",
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
    
    # Extract and convert form data to numeric values
    age = int(request.form["age"])
    sex = int(request.form["sex"])
    cp = int(request.form["cp"])
    trestbps = int(request.form["trestbps"])
    chol = int(request.form["chol"])
    fbs = int(request.form["fbs"])
    restecg = int(request.form["restecg"])
    thalach = int(request.form["thalach"])
    exang = int(request.form["exang"])
    oldpeak = float(request.form["oldpeak"])
    slope = int(request.form["slope"])
    ca = int(request.form["ca"])
    thal = int(request.form["thal"])
    
    # Create feature vector
    features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

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
