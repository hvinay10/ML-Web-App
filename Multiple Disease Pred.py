# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 15:20:09 2025

@author: vinay
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the Model's

diabetes_model = pickle.load(open('C:/Users/vinay/OneDrive/Desktop/Multiple Disease Predictor/trained_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/vinay/OneDrive/Desktop/Multiple Disease Predictor/heart.sav','rb'))

parkinson_model = pickle.load(open('C:/Users/vinay/OneDrive/Desktop/Multiple Disease Predictor/pakinson.sav','rb'))

# Sidebar for Navigation bar (It shows the option's for Disease)

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System",
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction System'],
                           
                           icons = ['activity','heart-pulse','person'],
                           
                           default_index = 0)
                           
# Diabetes Prediction Page

if (selected == 'Diabetes Prediction' ):
    
    # Page Title 
    
    st.title("Diabetes Prediction System")
    
    # No of i/p rows for values 
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age = st.text_input('Age of the Person')
        
    
        
    
    # Code for prediction
    
    diab_diagnosis = ''
    
    # Creating button for Prediction
    
    if st.button('Diabetes Test Results '):
        
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            
            diab_diagnosis = "The Person Diabetic"
        else:
            diab_diagnosis = "The Person is not Diabetic"
            
    # It Display's the Result
    
    st.success(diab_diagnosis)
        
    
    
    
    
    
# Heart Disease Prediction Page

# Heart Disease Prediction Page

if (selected == 'Heart Disease Prediction' ):
    
    # Page Title 
    st.title("Heart Disease Prediction System")
    
    # No of i/p rows for values 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of a Person')
        
    with col2:
        sex = st.text_input('Gender 0: F , 1:M')
        
    with col3:
        cp = st.text_input('Chest Pain Type')
        
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
        
    with col2:
        chol = st.text_input(' Serum Cholesterol  mg / dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg / dl || 0:F')
        
    with col1:
        restecg = st.text_input('Resting_Electrocardiographic_Results 0:Normal')
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina || 0 : No')
        
    with col1:
        oldpeak = st.text_input('ST Depression')
        
    with col2:
        slope = st.text_input('Slope_of_Peak||UpSlope : 0, Flat : 1, DownSlope : 2')
        
    with col3:
        ca = st.text_input('Number of Major Vessels')
        
    with col1:
        thal = st.text_input('1 = Fixed defect; 2 = Normal; 3 = Reversible_defect')
    
    # Code for prediction
    heart_diagnosis = ''
    
    # Creating button for Prediction
    if st.button('Heart Test Results'):
        try:
            # Convert all inputs to float
            input_data = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]

            heart_prediction = heart_model.predict([input_data])
             
            if (heart_prediction[0] == 1):
                heart_diagnosis = "The Person is Having Heart Disease"
            else:
                heart_diagnosis = "The Person is not Having Heart Disease"

        except ValueError:
            heart_diagnosis = "Please enter valid numeric values for all fields."
            
    # It Display's the Result
    st.success(heart_diagnosis)

    
    
    
# Parkinsons Page 

# Parkinsons Page 

if (selected == 'Parkinsons Prediction System' ):
    
    # Page Title 
    st.title("Parkinsons Prediction System")
    
    # No of i/p rows for values 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.text_input('Fo(Hz)')
        
    with col2:
        fhi = st.text_input('Fhi(Hz)')
        
    with col3:
        flo = st.text_input('Flo(Hz)')
        
    with col1:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
        
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col3:
        RAP = st.text_input('MDVP:RAP')
        
    with col1:
        PPQ = st.text_input('MDVP:PPQ')
    
    with col2:
        DDP = st.text_input('Jitter:DDP')
        
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA = st.text_input('Shimmer:DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
    
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col1:
        spread1 = st.text_input('Spread1')
        
    with col2:
        spread2 = st.text_input('Spread2')
        
    with col3:
        D2 = st.text_input('D2')
        
    with col1:
        PPE = st.text_input('PPE')
    
    # Code for prediction
    parkinson_diagnosis = ''
    
    # Creating button for Prediction
    if st.button('Parkinsons Test Results '):
        try:
            # Convert inputs to float
            input_data = [
                float(fo), float(fhi), float(flo), float(Jitter_percent),
                float(Jitter_Abs), float(RAP), float(PPQ), float(DDP),
                float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5),
                float(APQ), float(DDA), float(NHR), float(HNR),
                float(RPDE), float(DFA), float(spread1), float(spread2),
                float(D2), float(PPE)
            ]
            
            parkinson_prediction = parkinson_model.predict([input_data])
             
            if (parkinson_prediction[0] == 1):
                
                parkinson_diagnosis = "The Person has Parkinson's Disease"
            else:
                parkinson_diagnosis = "The Person does not Have Parkinson's Disease"
        
        except ValueError:
            parkinson_diagnosis = "Please enter valid numeric values for all fields."
            
    # It Display's the Result
    st.success(parkinson_diagnosis)
