# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:05:00 2023

@author: dell1
"""

import pickle,bz2
import streamlit as st
import numpy as np
scalarobject=bz2.BZ2File('Model/standardScalar.pkl', 'rb')
scaler=pickle.load(scalarobject)
modelforpred = bz2.BZ2File("Model/modelForPrediction.pkl", "rb")
model = pickle.load(modelforpred)
                                
                                
def patient_condition(input_data):
    input_data_array = np.asarray(input_data)
    input_data_scaled = scaler.transform(input_data_array)
    input_data_reshape = input_data_scaled.reshape(1,-1)
    prediction = model.predict(input_data_reshape)
    print(prediction)
    
    if (prediction[0] == 0):
        return 'The patient is Normal'
    elif (prediction[0] == 1):
        return 'The patient is Type H'
    else:
        return 'The patient is Type S'
    st.success(input_data_reshape)
def main():
    st.title("Patient Condition Prediction")
    st.header("Enter the value of the following parameters:")
    P_incidence	 = st.number_input("Enter the value of P_incidence")
    P_tilt	 = st.number_input("Enter the value of P_tilt")
    L_angle	 = st.number_input("Enter the value of L_angle")
    S_slope	 = st.number_input("Enter the value of S_slope")
    P_radius = st.number_input("Enter the value of P_radius")
    S_Degree = st.number_input("Enter the value of S_degree")
    
    
    patient_con = ' '
    
    if st.button('Predict Patient condition'):
        patient_con=patient_condition([[P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree]])
    st.success(patient_con)
    
if __name__ == '__main__':
    main()
    