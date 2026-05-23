import streamlit as st
import requests

st.header("BMI Calculator")

height = st.number_input('Enter your height in cms:')
weight = st.number_input('Enter your weight in kgs:')

if st.button('My BMI'): 
    response = requests.get("https://restapis-m9t8.onrender.com//bmi",
                        params={"weight":weight,"height":height})
    data = response.json()
    st.success(f"BMI: {data["BMI"]}")
    st.info(f"Category: {data["category"]}")
