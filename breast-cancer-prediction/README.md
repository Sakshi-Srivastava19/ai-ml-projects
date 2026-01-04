# 🩺 Breast Cancer Prediction App

This is a web app built with **Streamlit** that predicts whether a breast tumor is **Benign (non-cancerous)** or **Malignant (cancerous)** using a **Logistic Regression** model trained on the Breast Cancer Wisconsin dataset.

---
## link of app: https://breast-cancer-ezcuswhwksvaskj4c4moxh.streamlit.app/

## 🚀 Features

- 🔮 Predicts cancer diagnosis based on top 10 medical features
- 📊 Shows prediction confidence
- ✅ Simple UI with helpful feature explanations
- ⚙️ Built with scikit-learn and Streamlit

---

## 📦 Files in This Repo

| File                  | Description                                      |
|-----------------------|--------------------------------------------------|
| `app.py`              | Main Streamlit app file                          |
| `logistic_model.pkl`  | Trained logistic regression model (optional)     |
| `scaler.pkl`          | Fitted StandardScaler for input features         |
| `requirements.txt`    | Python dependencies                              |
| `README.md`           | You’re reading it 😉                              |

---

## 🧪 Input Features Used (Top 10)

- `radius_mean`
- `perimeter_mean`
- `area_mean`
- `concave points_mean`
- `concavity_mean`
- `compactness_mean`
- `radius_worst`
- `perimeter_worst`
- `area_worst`
- `concave points_worst`

Each feature represents a measurement extracted from cell nuclei images in breast mass biopsies.

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/breast-cancer-prediction.git
cd breast-cancer-streamlit
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate        # For Linux/Mac
venv\Scripts\activate           # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App
```bash
streamlit run app.py

```

## 🧠 Model Details

Algorithm: Logistic Regression

Preprocessing: StandardScaler

Dataset: Breast Cancer Wisconsin (Diagnostic)

Target Classes:

0 → Benign

1 → Malignant

## 🚀 Deployment

This app is deployed using Streamlit Community Cloud.

To deploy your own version:

Push code to GitHub

Go to https://streamlit.io/cloud

Select repo → app.py

Click Deploy

## 📌 Tech Stack

Python

Streamlit

scikit-learn

NumPy

Pandas

Pickle

### 👩‍💻 Author

Sakshi
📊 Data Science & AI Enthusiast

## ⭐ Acknowledgements

UCI Machine Learning Repository

Streamlit Documentation

scikit-learn Community

## ⭐ If you found this project useful, consider giving it a star!
