## 🧪 Glucose Level Predictor Web App
An interactive and user-friendly web application to predict whether a person has high glucose levels based on various health indicators. The app supports individual and batch predictions, bilingual labels (English & Hindi), and a modern UI with chart-based probability visualization.

## 🌐 Live Demo
Deploy using Render-
[https://glucose-predictor.onrender.com]

--- 
## 🛠️ Features
✅ Predict glucose level status (Normal or High)

📊 Bar chart showing prediction probability

🌍 Multilingual support (English & Hindi)

📤 Upload CSV for batch predictions

🎨 Responsive UI with background image

📚 Descriptions for each input feature

---

## 🖥️ Technologies Used
Python (Flask, NumPy, Pandas, scikit-learn, joblib)

HTML5, CSS3, Bootstrap 5

Chart.js for visualizing prediction probabilities


---

## �� Input Features

| Feature             | Description                      |
| ------------------- | -------------------------------- |
| `age`               | Patient's age in years           |
| `bmi`               | Body Mass Index (weight/height²) |
| `blood_pressure`    | Systolic blood pressure in mm Hg |
| `insulin`           | Insulin level (mu U/ml)          |
| `skin_thickness`    | Skinfold thickness in mm         |
| `glucose`           | Glucose concentration in mg/dL   |
| `pregnancies`       | Number of pregnancies            |
| `diabetes_pedigree` | Diabetes pedigree function value |

---

## 🛠️ Technologies Used

* **Python** with **Flask**
* **scikit-learn**, **NumPy**, **pandas**
* **HTML**, **Bootstrap 5**, **Chart.js**
* **Jinja2** for templating

---

## 💻 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/glucose-predictor.git
   cd glucose-predictor
   ```

2. **Create virtual environment**

   ```bash
   python -m venv glucose_env
   glucose_env\Scripts\activate  # For Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

5. Open `http://localhost:5000` in your browser

---

## 📄 Batch Prediction Format

Upload a `.csv` with the following columns:

```
age,bmi,blood_pressure,insulin,skin_thickness,glucose,pregnancies,diabetes_pedigree
```

The app returns predictions for all records in the file.

---

## 📁 Project Structure

```
glucose-predictor/
├── app.py
├── glucose_model.pkl
├── glucose_scaler.pkl
├── glucose_features.pkl
├── templates/
│   └── index.html
├── static/ (optional for assets)
├── requirements.txt
```

---

## 📜 License

MIT License © 2025 Sakshi Srivastava

---

## 🙏 Acknowledgments

* [PIMA Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* [Chart.js](https://www.chartjs.org/)
* [Bootstrap](https://getbootstrap.com/)
