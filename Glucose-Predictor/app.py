from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

# Load model components
model = joblib.load("glucose_model.pkl")
scaler = joblib.load("glucose_scaler.pkl")
features = joblib.load("glucose_features.pkl")

# Optional: Use predict_proba if supported
has_proba = hasattr(model, "predict_proba")

# Feature descriptions in English + Hindi
descriptions = {
    'age': 'Age of the person / व्यक्ति की उम्र',
    'BMI': 'Body Mass Index / शरीर द्रव्यमान सूचकांक',
    'totChol': 'Total cholesterol level / कुल कोलेस्ट्रॉल स्तर',
    'sysBP': 'Systolic blood pressure / सिस्टोलिक रक्तचाप',
    'diaBP': 'Diastolic blood pressure / डायस्टोलिक रक्तचाप',
    'heartRate': 'Heart rate in beats per minute / हृदय गति',
    'cigsPerDay': 'Cigarettes smoked per day / प्रतिदिन धूम्रपान',
    'education': 'Education level (1-4) / शिक्षा स्तर',
    'BPMeds': 'On BP medication (0/1) / बीपी की दवा ले रहे हैं',
    'prevalentStroke': 'History of stroke? (0/1) / स्ट्रोक का इतिहास',
    'prevalentHyp': 'Hypertension? (0/1) / उच्च रक्तचाप',
    'diabetes': 'Has diabetes? (0/1) / मधुमेह है?'
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", features=features, descriptions=descriptions)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [float(request.form[feature]) for feature in features]
        input_scaled = scaler.transform([input_data])
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1] if has_proba else None
        result = "High Glucose Level Detected" if prediction == 1 else "Glucose Level is Normal"

        return render_template("index.html", features=features, descriptions=descriptions,
                               result=result, probability=round(probability, 2) if probability else None)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/batch', methods=['POST'])
def batch_predict():
    try:
        file = request.files['file']
        df = pd.read_csv(file)

        missing_cols = [col for col in features if col not in df.columns]
        if missing_cols:
            return f"Missing columns in uploaded CSV: {', '.join(missing_cols)}"

        X = scaler.transform(df[features])
        predictions = model.predict(X)
        df['Prediction'] = ['High Glucose' if p == 1 else 'Normal' for p in predictions]

        result_html = df.to_html(classes='table table-bordered', index=False)
        return f"<h4>Prediction Results:</h4>{result_html}<br><a href='/'>Back</a>"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
