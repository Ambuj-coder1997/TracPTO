import streamlit as st
import pickle
import numpy as np
#from PIL import Image
from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#image = Image.open('FuelPredx_logo.jpg')

def load_model():
    with open('Engine_PTO_Power_gbr_saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]

def show_predict_page():

    st.markdown("<h1 style='text-align: center; color: DarkGoldenRod;'>TracPTO</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: DarkGreen;'> Cloud-driven Serverless Architecture for real-time Engine PTO power prediction of Tractor </h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: DarkRed;'>Input the following tractor operating parameters for predicting the real-time PTO Power of tractor : </h3>", unsafe_allow_html=True)

    #st.sidebar.image(image, use_column_width=True)
    TractorPTOPower = st.number_input('Tractor PTO power (hp)')
    Tractor_PTO2 = TractorPTOPower / 1.36
    Engine_Speed = st.number_input('Engine operating speed (rpm)')
    Speed_Depression = st.number_input('Engine speed depression (rpm)')

    #Tractor_PTO = st.number_input('Tractor maximum PTO power (hp)')
    #Tractor_PTO2 = Tractor_PTO/1.36
    #Engine_Speed = st.number_input('Engine operating speed (rpm)')
    #Speed_Depression = st.number_input('Engine speed depression (rpm)')

    ok = st.button("Predict real-time PTO Power")
    if ok:
        X = np.array([[Tractor_PTO2, Engine_Speed, Speed_Depression]])
        #Y = sc.transform(X)
        #Y = Y.astype(float)
        X = X.astype(float)
        salary = regressor.predict(X)
        salary2 = salary*1.36
        st.subheader(f"The estimated Instantaneous PTO Power(hp) is {salary2[0]:.2f}")



