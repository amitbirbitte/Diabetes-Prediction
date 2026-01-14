from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("Diabetes-Prediction-model.pkl", "rb"))

@app.route("/")
def landing():
    return render_template("home.html")   # landing page image here

@app.route("/home")
def home():
    return render_template("index.html")  # input form


@app.route("/predict", methods=["POST"])
def predict():
    try:
        Pregnancies = float(request.form.get( "Pregnancies"))
        Glucose = float(request.form.get("Glucose"))
        BloodPressure = float(request.form.get("BloodPressure"))
        SkinThickness = float(request.form.get("SkinThickness"))
        Insulin = float(request.form.get("Insulin"))
        BMI = float(request.form.get("BMI"))
        DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
        Age = float(request.form.get("Age"))

        input_data = pd.DataFrame([[
            Pregnancies, Glucose, BloodPressure,
            SkinThickness, Insulin, BMI,
            DiabetesPedigreeFunction, Age
        ]], columns=[
            "Pregnancies", "Glucose", "BloodPressure",
            "SkinThickness", "Insulin", "BMI",
            "DiabetesPedigreeFunction", "Age"
        ])

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "⚠️ High Risk of Diabetes"
            color = "red"
        else:
            result = "✅ Low Risk of Diabetes"
            color = "green"

        return render_template("result.html", result=result, color=color)

    except Exception as e:
        return render_template(
            "result.html",
            result=f"Error occurred: {str(e)}",
            color="orange"
        )

if __name__ == "__main__":
    app.run(debug=True)
