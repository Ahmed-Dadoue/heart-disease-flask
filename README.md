# ❤️ Heart Disease Prediction Flask App 💊

A professional, multilingual medical prediction system built with Flask and Machine Learning. Predict heart disease risk using clinical data with an intuitive, user-friendly interface.

## 🌍 Live Demo

🔗 **[heart-disease-flask.onrender.com](https://heart-disease-flask-2ue3.onrender.com)**

## ✨ Features

### 🎯 Core Functionality
- **ML Model**: RandomForest Classifier for heart disease prediction
- **Multilingual**: English, Deutsch, العربية (RTL support)
- **Medical Data Input**: 13 clinical parameters
- **Risk Assessment**: 3-level risk categorization with visual feedback
- **Professional UI**: Modern Teal design with responsive layout

### 📊 Advanced Features
- **Interactive Info Boxes**: 3-layer information system (What/Select/Source)
- **Source Badges**: Indicates data source (Blood Test, ECG, Stress Test, Specialist)
- **Medical Warnings**: ⚠️ Badges for fields requiring specialist reports
- **Progress Bar**: Visual representation of risk percentage
- **Color-Coded Results**:
  - 🟢 Green (<40%) = Low Risk
  - 🟡 Yellow (40-70%) = Moderate Risk
  - 🔴 Red (>70%) = High Risk
- **Form Validation**: Real-time field validation with visual feedback
- **Reset Button**: Quick form clearing
- **Professional Results Display**: Disclaimer + Recommendation section

### 🎨 Design
- Modern Teal/Cyan color scheme (#06b6d4)
- Gradient backgrounds and shadows
- Medical icons (❤️ 💊)
- Smooth animations and transitions
- Mobile-responsive design
- RTL support for Arabic

## 📋 Medical Fields

1. **Age** - Patient age in years (29-77)
2. **Sex** - Male/Female
3. **Chest Pain Type** - Typical/Atypical/Non-Anginal/Asymptomatic
4. **Resting BP** - Blood pressure in mm Hg
5. **Cholesterol** - Serum cholesterol in mg/dl
6. **Fasting Blood Sugar** - >120 mg/dl indicator
7. **Resting ECG** - Normal/ST-T Abnormality/LVH
8. **Max Heart Rate** - Peak rate during exercise
9. **Exercise Angina** - Yes/No
10. **ST Depression** - Exercise-induced (0-6.2)
11. **ST Slope** - Upsloping/Flat/Downsloping
12. **Major Vessels** - Count from imaging (0-4)
13. **Thalassemia** - Normal/Fixed/Reversible defect

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Local Setup

```bash
# Clone repository
git clone https://github.com/Ahmed-Dadoue/heart-disease-flask.git
cd heart-disease-flask

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python src/app_flask.py
```

Visit: **http://localhost:5000** 🌐

## 📦 Dependencies

```
Flask - Web framework
scikit-learn==1.6.1 - Machine learning
joblib - Model serialization
gunicorn - Production server
numpy - Numerical computing
pandas - Data processing
```

## 📂 Project Structure

```
heart-disease-flask/
├── src/
│   └── app_flask.py          # Main Flask application
├── templates/
│   └── index.html            # HTML template with 3 languages
├── static/
│   └── styles.css            # Modern CSS with Teal theme
├── model/
│   └── pipeline.joblib       # Trained RandomForest model
├── requirements.txt          # Python dependencies
├── render.yaml              # Render deployment config
└── README.md                # This file
```

## 🛠️ Technology Stack

**Backend**
- Flask 3.x
- scikit-learn 1.6.1
- Python 3.14+

**Frontend**
- HTML5 / Jinja2 Templates
- CSS3 (Gradients, Flexbox, Grid)
- Vanilla JavaScript (No frameworks)

**Deployment**
- Render.com (Production)
- GitHub (Version Control)
- Gunicorn (WSGI Server)

## 🌐 Multilingual Support

- **English (EN)** - Full UI in English
- **Deutsch (DE)** - Complete German translation
- **العربية (AR)** - Full Arabic with RTL support

Language switcher in top-right corner allows instant switching.

## 📊 Model Information

- **Algorithm**: RandomForest Classifier
- **Training Data**: Cleveland Heart Disease Dataset
- **Features**: 13 clinical parameters
- **Output**: Binary classification (0=Low Risk, 1=High Risk)
- **Confidence**: Probability score (0-100%)

## 🎯 How to Use

1. **Select Language** 🌍
   - Click EN/DE/العربية in top-right

2. **Review Information** ℹ️
   - Read the important note banner
   - Click ⓘ icons for detailed field explanations
   - Check source badges for data origin

3. **Enter Medical Data** 📝
   - Fill in all 13 fields with accurate values
   - Use dropdown for categorical fields
   - Enter numbers for numeric fields

4. **Get Prediction** 🔮
   - Click "Predict" button
   - View results with risk level and percentage
   - Read disclaimer and recommendations

5. **Reset or Retry** 🔄
   - Click "Reset Form" to clear all fields
   - Re-enter different values for new prediction

## ⚠️ Medical Disclaimer

**This application is for educational purposes only.**

- NOT a medical diagnosis tool
- Results are estimates based on input data
- Always consult a healthcare professional
- Do not use for clinical decision-making
- Accuracy depends on data accuracy

## 🚀 Deployment to Render

### Automatic Deployment (GitHub Integration)
1. Push code to GitHub
2. Render automatically rebuilds and deploys
3. Live at: https://heart-disease-flask-2ue3.onrender.com

### Manual Deployment
1. Visit [render.com](https://render.com)
2. Create new Web Service
3. Connect GitHub repository
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn --chdir src app_flask:app`
6. Deploy

## 📝 Recent Updates (Phase 1 & 2)

### Phase 1 - Enhanced User Guidance
- ✅ Expanded info boxes (What/Select/Source format)
- ✅ Medical field warnings (⚠️ badges)
- ✅ Important note banner
- ✅ All 3 languages complete

### Phase 2 - Professional Design
- ✅ Progress bar with color-coded fill
- ✅ Risk-level coloring (Green/Yellow/Red)
- ✅ Source badges (Blood Test/ECG/Stress Test/Specialist)
- ✅ Reset button
- ✅ Enhanced result display
- ✅ Professional medical design

### Phase 3 - Modern Aesthetics
- ✅ Teal/Cyan color scheme (#06b6d4)
- ✅ Gradient backgrounds
- ✅ Medical icons (❤️ 💊)
- ✅ Enhanced shadows and animations
- ✅ Professional typography

## 🔐 Security & Performance

- No user data storage
- HTTPS on Render deployment
- Fast model inference (<100ms)
- Responsive design (Mobile-first)
- XSS protection via Jinja2
- CSRF token support

## 📧 Contact & Support

- **GitHub**: [Ahmed-Dadoue/heart-disease-flask](https://github.com/Ahmed-Dadoue/heart-disease-flask)
- **Issues**: GitHub Issues for bug reports
- **Features**: Feature requests welcome!

## 📄 License

MIT License - Feel free to use and modify

## 💡 Future Enhancements

- ✨ Smart input validation (range checking)
- ✨ Sample data auto-fill button
- ✨ Form section grouping
- ✨ Advanced explanation levels
- ✨ Database for prediction history
- ✨ PDF report generation
- ✨ API endpoints

---

**Made with ❤️ for better heart health** 🏥

**Last Updated**: March 2026
