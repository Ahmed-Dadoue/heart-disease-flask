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
        "oldpeak": "ST Depression",
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
        "hint_sex": "Select your gender",
        "hint_age": "Enter your age in years (29-77)",
        "hint_cp": "Choose the type of chest pain you experience",
        "hint_trestbps": "Resting blood pressure in mm Hg",
        "hint_chol": "Serum cholesterol in mg/dl",
        "hint_fbs": "Based on your fasting blood sugar test",
        "hint_restecg": "Result from your resting electrocardiogram",
        "hint_thalach": "Maximum heart rate achieved during exercise",
        "hint_exang": "Do you experience chest pain with exercise?",
        "hint_oldpeak": "ST depression induced by exercise (0-6.2)",
        "hint_slope": "Slope of ST segment during exercise",
        "hint_ca": "Number of major vessels visible (0-4)",
        "hint_thal": "Thalassemia type from imaging",
        "info_sex": "Select your biological sex: Male = Man, Female = Woman.",
        "info_age": "Enter your current age in years. The values in this model range from 29 to 77.",
        "info_cp": "Choose the type of chest pain: Typical Angina = clear heart-related pain, Atypical Angina = similar to heart pain but not typical, Non-Anginal Pain = pain usually not from the heart, Asymptomatic = no obvious pain.",
        "info_trestbps": "This is your resting blood pressure in mm Hg. You can get this value from your medical report or blood pressure measurement.",
        "info_chol": "Enter your serum cholesterol level in mg/dl. This value is from your blood test report.",
        "info_fbs": "This field indicates whether your fasting blood sugar is greater than 120 mg/dl. Choose based on your test results.",
        "info_restecg": "Choose the result closest to your electrocardiogram: Normal = no apparent abnormality, ST-T Wave Abnormality = unusual changes in the ECG, Left Ventricular Hypertrophy = thickening of the left heart muscle.",
        "info_thalach": "Enter the maximum heart rate you achieved during exercise testing. This value is from your cardiac test report.",
        "info_exang": "Do you experience chest pain or angina when exercising or using effort? Choose Yes or No.",
        "info_oldpeak": "This is the ST depression value from your cardiac test. It represents how much the ST segment drops during exercise. If you don't know it, get it from your medical report.",
        "info_slope": "This describes the shape of the ST segment under stress: Upsloping, Flat, or Downsloping. Choose based on your test results.",
        "info_ca": "This is the number of major blood vessels visible in your cardiac imaging. Usually between 0 and 4.",
        "info_thal": "This field is related to thalassemia test results: Normal = no abnormality, Fixed Defect = permanent defect, Reversible Defect = defect that may vary.",
        "help_button": "How to fill this form?",
        "help_text": "Fill in the medical values as they appear in your medical report. For fields with dropdown arrows, select from the options. If you don't understand a field, click the ⓘ icon next to it for more details. Don't enter random values—use your actual medical data.",
        "validation_error": "Please fill in all required fields correctly before submitting.",
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
        "oldpeak": "ST-Senkung",
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
        "hint_sex": "Wählen Sie Ihr Geschlecht",
        "hint_age": "Geben Sie Ihr Alter in Jahren ein (29-77)",
        "hint_cp": "Wählen Sie die Art der Brustschmerzen",
        "hint_trestbps": "Ruheblutdruck in mm Hg",
        "hint_chol": "Serumcholesterin in mg/dl",
        "hint_fbs": "Basierend auf Ihrem Nüchternbluttest",
        "hint_restecg": "Ergebnis aus Ihrem Ruhe-EKG",
        "hint_thalach": "Maximale Herzfrequenz erreicht während Bewegung",
        "hint_exang": "Verspüren Sie Brustschmerzen bei Anstrengung?",
        "hint_oldpeak": "ST-Senkung durch Belastung (0-6.2)",
        "hint_slope": "Steigung des ST-Segments während Belastung",
        "hint_ca": "Anzahl der sichtbaren Arterien (0-4)",
        "hint_thal": "Thalassämie-Typ aus Bildgebung",
        "info_sex": "Wählen Sie Ihr biologisches Geschlecht: Männlich = Mann, Weiblich = Frau.",
        "info_age": "Geben Sie Ihr aktuelles Alter in Jahren ein. Die Werte in diesem Modell liegen zwischen 29 und 77.",
        "info_cp": "Wählen Sie die Art der Brustschmerzen: Typische Angina = klarer herzabhängiger Schmerz, Atypische Angina = ähnlich wie Herzschmerz, aber nicht typisch, Nicht-anginöse Schmerzen = Schmerzen, die normalerweise nicht vom Herzen stammen, Asymptomatisch = kein offensichtlicher Schmerz.",
        "info_trestbps": "Dies ist Ihr Ruheblutdruck in mm Hg. Sie können diesen Wert aus Ihrem Bericht oder Blutdruckmessung abrufen.",
        "info_chol": "Geben Sie Ihren Serumcholesterinwert in mg/dl ein. Dieser Wert stammt aus Ihrem Bluttestbericht.",
        "info_fbs": "Dieses Feld gibt an, ob Ihr Nüchternblutzucker höher als 120 mg/dl ist. Wählen Sie basierend auf Ihren Testergebnissen.",
        "info_restecg": "Wählen Sie das Ergebnis, das Ihrem EKG am nächsten kommt: Normal = keine offensichtliche Anomalie, ST-T-Wellen-Anomalie = ungewöhnliche Veränderungen im EKG, Linksventrikuläre Hypertrophie = Verdickung der Herzmuskulatur.",
        "info_thalach": "Geben Sie die maximale Herzfrequenz ein, die Sie während der Belastungsprüfung erreicht haben. Dieser Wert stammt aus Ihrem Herzbericht.",
        "info_exang": "Verspüren Sie bei Belastung oder Anstrengung Brustschmerzen? Wählen Sie Ja oder Nein.",
        "info_oldpeak": "Dies ist der ST-Senkungswert aus Ihrem Herztest. Wählen Sie basierend auf Ihrem Bericht.",
        "info_slope": "Dies beschreibt die Form des ST-Segments unter Stress: Ansteigend, Flach oder Absteigend.",
        "info_ca": "Dies ist die Anzahl der Blutgefäße in Ihrem Herzbildgebung. Normalerweise zwischen 0 und 4.",
        "info_thal": "Dieses Feld bezieht sich auf Thalassämie-Testergebnisse: Normal = keine Anomalie, Festgestellter Defekt = permanenter Defekt, Reversibler Defekt = Defekt, der variieren kann.",
        "help_button": "Wie fülle ich dieses Formular aus?",
        "help_text": "Füllen Sie die medizinischen Werte aus, wie sie in Ihrem Bericht stehen. Für Felder mit Dropdown-Pfeilen wählen Sie aus den Optionen. Wenn Sie ein Feld nicht verstehen, klicken Sie auf das ⓘ-Symbol daneben. Geben Sie keine zufälligen Werte ein.",
        "validation_error": "Bitte füllen Sie alle erforderlichen Felder korrekt aus, bevor Sie das Formular einreichen.",
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
        "hint_sex": "اختر الجنس من القائمة",
        "hint_age": "أدخل العمر بالسنوات (29-77)",
        "hint_cp": "اختر الوصف الأقرب لنوع الألم الذي تشعر به",
        "hint_trestbps": "يكتب بوحدة mm Hg",
        "hint_chol": "أدخل قيمة الكوليسترول في الدم",
        "hint_fbs": "اختر القيمة المناسبة بناءً على التحليل",
        "hint_restecg": "اختر النتيجة الأقرب من التقرير الطبي",
        "hint_thalach": "أدخل أعلى معدل نبض تم الوصول إليه",
        "hint_exang": "هل يظهر ألم صدري عند الجهد؟",
        "hint_oldpeak": "أدخل قيمة ST depression",
        "hint_slope": "اختر شكل انحدار ST أثناء الجهد",
        "hint_ca": "عدد الأوعية الرئيسية الملونة بالفحص",
        "hint_thal": "اختر الحالة حسب نتيجة الفحص",
        "info_sex": "اختر الجنس البيولوجي: ذكر = رجل، أنثى = امرأة.",
        "info_age": "أدخل عمرك الحالي بالسنوات. القيم في هذا النموذج تتراوح بين 29 و 77 سنة.",
        "info_cp": "اختر نوع ألم الصدر: ذبحة نموذجية = ألم واضح مرتبط بالقلب، ذبحة غير نموذجية = ألم يشبه ألم القلب لكنه ليس نمطياً، ألم غير ذبحي = ألم غالباً ليس من القلب، بدون أعراض = لا يوجد ألم واضح.",
        "info_trestbps": "هذا ضغط دمك أثناء الراحة بوحدة mm Hg. يمكنك الحصول على هذه القيمة من التقرير الطبي أو قياس ضغط الدم.",
        "info_chol": "أدخل قيمة الكوليسترول في الدم بوحدة mg/dl. تأتي هذه القيمة من تقرير فحص الدم.",
        "info_fbs": "هذا الحقل يعني: هل سكر الدم الصائم أكبر من 120 mg/dl؟ اختر بناءً على نتائج التحليل.",
        "info_restecg": "اختر النتيجة الأقرب من تقرير تخطيط القلب: طبيعي = لا يوجد خلل ظاهر، اضطراب ST-T = تغيرات غير طبيعية في موجات التخطيط، تضخم البطين الأيسر = زيادة في سماكة عضلة البطين الأيسر.",
        "info_thalach": "أدخل أعلى معدل نبض تم الوصول إليه أثناء اختبار الجهد. هذه القيمة من تقرير فحص القلب.",
        "info_exang": "هل تشعر بألم صدري أو ذبحة عند بذل الجهد أو الحركة؟ اختر نعم أو لا.",
        "info_oldpeak": "هذه قيمة من تقرير الفحص القلبي وتمثل مقدار انخفاض ST أثناء الجهد مقارنة بالراحة. إذا كنت لا تعرفها، خذها من التقرير الطبي.",
        "info_slope": "هذا يصف شكل انحدار ST أثناء الجهد: صاعد، مسطح، أو هابط. اختره حسب نتيجة الفحص.",
        "info_ca": "هذا الرقم يعبر عن عدد الأوعية الرئيسية التي ظهرت في الفحص. غالباً تكون القيمة بين 0 و 4.",
        "info_thal": "هذا الحقل مرتبط بنتيجة فحص thal: طبيعي = لا يوجد خلل، عيب ثابت = خلل ثابت، عيب قابل للعكس = خلل يظهر ويمكن أن يتغير.",
        "help_button": "كيف أملأ هذا النموذج؟",
        "help_text": "املأ القيم الطبية كما هي في التقرير الطبي. الحقول التي تحتوي على سهم هي قوائم اختيار. إذا لم تفهم معنى أي حقل، اضغط على الرمز ⓘ بجانب اسم الحقل. لا تدخل قيماً عشوائية - استخدم بيانات طبية فعلية.",
        "validation_error": "يرجى ملء جميع الحقول المطلوبة بشكل صحيح قبل الإرسال.",
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
