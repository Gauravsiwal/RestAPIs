import streamlit as st
import requests

st.header("BMI Calculator")

height = st.number_input('Enter your height in cms:')
weight = st.number_input('Enter your weight in kgs:')

if st.button('My BMI'): 
    response = requests.get("http://127.0.0.1:8000/bmi",
                        params={"weight":weight,"height":height})
    data = response.json()
    st.success(f"BMI: {data['bmi']}")
    st.info(f"Category: {data['category']}")
