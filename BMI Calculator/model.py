import streamlit as st
import numpy as np
import pickle as pkl
model = pkl.load(open('model.pkl', 'rb'))
st.title("Body Mass Index (BMI) Calculator")
height = st.number_input("Enter Height in Meters")
weight = st.number_input("Enter Weight in Kg")
if st.button('Calculate'):
    value = weight / np.power(height, 2)
    result = model.predict([[value]])
    st.title(f"Your BMI Score = {result[0]}")
    if result == 0:
        st.title("Normal")
    elif result == 1:
        st.title("Over Weight")
    else: st.title('Under Weight')
st.title('Design and Develop by Abhisek')
st.text('A Machine Learning Project')
st.header('Check Git Hub Repo')
st.write('https://github.com/abhisekadhikari/Machine-Learning')
st.header('Give Me a Star')
st.write('https://github.com/abhisekadhikari/')