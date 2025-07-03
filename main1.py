import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("logistic_model_loan.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Loan Approval Predictor")

feature_names = [
    "ApplicantIncome",    "Co-applicantIncome",    "LoanAmount",   "Loan_Amount_Term",
    "Credit_History(1/Yes , 0/No)",  "Gender(0/Female, 1/Male)",  "Married(0/No, 1/Yes)",  
    "Dependents(1,2,3)","Education(0/Not Graduate, 1/Graduate)","Self_Employed(0/No, 1/Yes)",   "Property_Area(0/Urban, 1/Semiurban, 2/Rural)"
]


values = []
for i in feature_names:
    value = st.number_input(f"Enter {i}", value=0.0)
    values.append(value)


if  st.button("Predict Loan Approval"):
    input_array = np.array([values])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
