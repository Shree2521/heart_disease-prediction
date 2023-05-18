import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
# diabetes_model=pickle.load(open("C:/Users/tharu/OneDrive/Desktop/DMT/heart.pickle",'rb'))


heart_disease_model=pickle.load(open(C:/Users/Shreeshree/Desktop/DMT/heart_model.pickle))





#sidebar

# with st.sidebar:
#     selected=option_menu("Heart Disease prediction system",
#                          ['Heart disease  prediction',
#                           'Diabetes  prediction',
#                           'parkinsons disease prediction'],
#                           icons=['heart','activity','person'],
#                           default_index=0)

#diabetes prediction


# if (selected=='Heart disease  prediction'):
    
    #st.title
st.title('Heart disease prediction using ML')
    
col1, col2, col3 = st.columns(3)
    
with col1:
        age = st.text_input('Age')
        
with col2:
        sex = st.text_input('Sex')
        
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
        
# Convert input values to numeric format
if age.isnumeric():
    age = float(age)
else:
    # Handle empty input value
    age = 0.0  # Assign a default value or raise an error, depending on your requirements

if sex.isnumeric():
    sex = float(sex)
else:
    # Handle empty input value
    sex = 0.0

if cp.isnumeric():
    cp = float(cp)
else:
    # Handle empty input value
    cp = 0.0

if trestbps.isnumeric():
    trestbps = float(trestbps)
else:
    # Handle empty input value
    trestbps = 0.0

if chol.isnumeric():
    chol = float(chol)
else:
    # Handle empty input value
    chol = 0.0

if fbs.isnumeric():
    fbs = float(fbs)
else:
    # Handle empty input value
    fbs = 0.0

if restecg.isnumeric():
    restecg = float(restecg)
else:
    # Handle empty input value
    restecg = 0.0

if thalach.isnumeric():
    thalach = float(thalach)
else:
    # Handle empty input value
    thalach = 0.0

if exang.isnumeric():
    exang = float(exang)
else:
    # Handle empty input value
    exang = 0.0

if oldpeak.isnumeric():
    oldpeak = float(oldpeak)
else:
    # Handle empty input value
    oldpeak = 0.0

if slope.isnumeric():
    slope = float(slope)
else:
    # Handle empty input value
    slope = 0.0

if ca.isnumeric():
    ca = float(ca)
else:
    # Handle empty input value
    ca = 0.0

if thal.isnumeric():
    thal = float(thal)
else:
    # Handle empty input value
    thal = 0.0

# Pass numeric input values to the model for prediction
#heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
       
     
     
    # code for Prediction
heart_diagnosis = ''
    
    # creating a button for Prediction
    
if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
st.success(heart_diagnosis)