import os
import streamlit as st
import pandas as pd
import pickle



# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


st.title('Customer Churn Prediction - Upload CSV')

upload_block, notes_block = st.columns(2, border=True)

with upload_block:
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

with notes_block:
    st.write("Tutorial")
    st.write("1. Upload a CSV file containing the customer data.")
    st.write("2. Click on the 'Predict' button to make predictions.")
    st.write("3. The churn prediction will be displayed below.")
    st.write("4. Data must contain the following columns (THESE COLUMN NAMES MUST BE WRITTEN EXACTLY THE SAME WAY):")
    st.write("Dependents, Tenure, OnlineSecurity, OnlineBackup, InternetService, DeviceProtection, TechSupport, Contract, PaperlessBilling, MonthlyCharges")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(data)

    if st.button('Predict'):
        try:
            if data.isnull().values.any():
                st.error("Input data contains NaN values. Please check your input.")
            else:
                prediction = model.predict(data)
                probability = model.predict_proba(data)[:, 1] * 100
                probability = [f"{prob:.2f}%" for prob in probability]
                prediction = ['Churn' if pred == 1 else 'Not Churn' for pred in prediction]
                result_df = pd.DataFrame({
                    'Prediction': prediction,
                    'Churning Probability (%)': probability
                })
                st.write("Prediction Results:")
                st.dataframe(result_df)
        except Exception as e:
            st.error(f"Error in prediction: {e}")