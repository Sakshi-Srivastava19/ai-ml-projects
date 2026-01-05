# retrain_model.py
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("framingham.csv")
df = df.dropna()

# Select features
features = ['age', 'BMI', 'heartRate', 'sysBP', 'diaBP', 'glucose']
X = df[features]
y = (df['glucose'] > 100).astype(int)

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)

# Save
joblib.dump(model, "glucose_model.pkl")
joblib.dump(scaler, "glucose_scaler.pkl")
joblib.dump(features, "glucose_features.pkl")
