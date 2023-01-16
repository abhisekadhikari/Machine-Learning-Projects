import streamlit as st
import numpy as np
import pickle as pkl
st.set_page_config(page_title = 'Abhitech - BMI Calculator')
model = pkl.load(open('model.pkl', 'rb'))
st.title("Body Mass Index (BMI) Calculator")
height = st.number_input("Enter Height in Meters")
weight = st.number_input("Enter Weight in Kg")
if st.button('Calculate'):
    value = weight / np.power(height, 2)
    result = model.predict([[value]])
    st.title(f"Your BMI Score = {value}")
    if result == 0:
        st.title("Normal")
    elif result == 1:
        st.title("Over Weight")
    else: st.title('Under Weight')
st.title("What is body mass index ?")
st.text("Body Mass Index (BMI) is a person’s weight in kilograms (or pounds) divided by the square of height in meters (or feet). A high BMI can indicate high body fatness. BMI screens for weight categories that may lead to health problems, but it does not diagnose the body fatness or health of an individual.")
st.title('Design and Develop by Abhisek')
st.text('A Machine Learning Project')
st.header('Check Git Hub Repo')
st.write('https://github.com/abhisekadhikari/Machine-Learning')
st.header('Give Me a Star')
st.write('https://github.com/abhisekadhikari/')
