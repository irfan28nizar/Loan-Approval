# Loan Approval Predictor

This project is a Streamlit web app that predicts loan approval using a trained logistic regression model.

## Features

- User-friendly web interface for entering applicant details
- Predicts loan approval status based on input features
- Uses a pre-trained logistic regression model and scaler

## Files

- `main1.py`: Streamlit app source code
- `logistic_model_loan.pkl`: Trained logistic regression model
- `scaler.pkl`: Scaler used for feature normalization
- `the_loan (1).csv`: Dataset used for training
- `Muhammed Irfan Nizarudeen.ipynb`: Jupyter notebook for data processing and model training

## How to Run

1. Install requirements:
    ```sh
    pip install streamlit numpy
    ```

2. Start the app:
    ```sh
    streamlit run main1.py
    ```

3. Open the provided local URL in your browser.

## Usage

- Enter the required applicant and loan details in the input fields.
- Click "Predict Loan Approval" to see the prediction result.

## Author

Muhammed Irfan Nizarudeen
