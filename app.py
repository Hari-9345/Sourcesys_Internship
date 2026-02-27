import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
st.title("Student Marks Predictor")
st.write("Enter study hours to predict exam marks")
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
marks = np.array([35, 40, 50, 55, 65, 70, 80, 90])
model = LinearRegression()
model.fit(hours, marks)
study_hours = st.number_input("Enter Study Hours:", min_value=0.0, max_value=12.0, step=0.5)
if st.button("Predict Marks"):
    prediction = model.predict([[study_hours]])
    st.success(f"Predicted Marks: {prediction[0]:.2f}")
    
    if prediction[0] >= 50:
        st.info("Status: Pass ✅")
    else:
        st.warning("Status: Fail ❌")