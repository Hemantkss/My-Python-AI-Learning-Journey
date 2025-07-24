import streamlit as st
import pandas as pd
import numpy as np
import joblib 

model = joblib.load('KNN_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title("Heart Disease Prediction")
st.markdown("This is a web app to predict heart disease.")

age = st.slider("Age", 0, 100, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
resting_blood_pressure = st.number_input("Resting Blood Pressure", 0, 200, 120)
cholesterol = st.number_input("Cholesterol", 0, 600, 200)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar", ["Greater than 120 mg/dl", "Less than 120 mg/dl"])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_heart_rate_achieved = st.slider("Max Heart Rate Achieved", 0, 200, 120)
exercise_induced_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 0.0)
st_slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])

if st.button("Predict"):
    raw_input = {
        "age": [age],
        "sex": [sex],
        "chest_pain_type": [chest_pain_type],
        "resting_blood_pressure": [resting_blood_pressure],
        "cholesterol": [cholesterol],
        "fasting_blood_sugar": [fasting_blood_sugar],
        "resting_ecg": [resting_ecg],
        "max_heart_rate_achieved": [max_heart_rate_achieved],
        "exercise_induced_angina": [exercise_induced_angina],
        "oldpeak": [oldpeak],
        "st_slope": [st_slope]
    }
    
    input_df = pd.DataFrame([raw_input])
    
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    input_df = input_df[expected_columns]
    
    scaled_input = scaler.transform(input_df)
    
    prediction = model.predict(scaled_input)[0]
    
    if prediction == 1:
        st.error("Patient is likely to have heart disease.")
    else:
        st.success("Patient is unlikely to have heart disease.")