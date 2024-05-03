import os
import pickle
import streamlit as st
import time
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction",
                   layout="wide",
                   page_icon="heart"
                   )
# st.markdown("""
# <style>
# 	[data-testid="stDecoration"] {
# 		display: none;
# 	}

# </style>""",
# unsafe_allow_html=True)

st.markdown("""
<style>
    [data-testid="stDecoration"] {
        background: linear-gradient(to right, #0070f3, #ffffff);
        background-size: cover;
        background-position: center;
        display: block;
    }
    div.stButton > button:first-child {
        color: lightblue;
    }
    div.stButton > button:hover {
        color: blue;
        background-color: lightblue;
        border-color: blue;
    }
    div.stButton > button:active {
        color: blue;
        border-color: blue;
    }
    div.stButton > button:focus {
        border-color: blue !important;
        background-color: lightblue !important;
        color: blue !important;
        box-shadow: none !important;
    }
</style>        
""", unsafe_allow_html=True)

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

heart_disease_model = pickle.load(open(f'{working_dir}/heart_prediction_model.sav', 'rb'))

# page title
st.title('❤️ Heart Disease Prediction using ML')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex; 1 = male; 0 = female')

with col3:
    cp = st.text_input('Chest Pain types')

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholestoral in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results')

with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina')

with col1:
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    ca = st.text_input('Major vessels colored by flourosopy')

with col1:
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

# code for Prediction
heart_diagnosis = ''

# creating a button for Prediction

if st.button(label="Click to see Result", type="secondary"):
    with st.spinner('Wait for it...'):
        time.sleep(5)

    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    user_input = [float(x) for x in user_input]

    heart_prediction = heart_disease_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'

st.info(heart_diagnosis)
