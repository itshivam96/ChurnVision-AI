from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # ✅ THIS LINE FIXES YOUR ISSUE

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
        data["tenure_months"],
        data["monthly_charges"],
        data["support_tickets"],
        data["last_login_days"]
    ]])

    prob = model.predict_proba(features)[0][1]

    return jsonify({
        "churn_probability": float(prob),
        "risk": "HIGH" if prob > 0.7 else "LOW"
    })

if __name__ == "__main__":
    app.run(debug=True)