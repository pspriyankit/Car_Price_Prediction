import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# loading the saved models

car_model = pickle.load(open('Price_prediction.pkl', 'rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Prediction System',
                          
                          ['Car Price Prediction',
                           'House Price Prediction'],
                          icons=['gear','house'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Car Price Prediction'):
    
    # page title
    st.title('Car Price Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Year = st.text_input('Model Year')

        
    with col2:
        Present_Price = st.text_input('Showroom Price?(In lakhs)')
    
    with col3:
        Kms_Driven = st.text_input('How Many Kilometers Drived?')
        
    
    with col1:
        Owner = st.text_input('Count of previous owners(0 or 1 or 3) ?')
    
    with col2:
        
        Fuel_Type_Petrol = st.selectbox(
                             'What Is the Fuel type?',
                             ('Petrol', 'Diesel', 'CNG'))
        
    
    with col3:
        Seller_Type_Individual = st.selectbox(
                             'Are you A Dealer or Individual',
                             ('Dealer', 'Individual'))
        
        
        
    
    with col1:
        Transmission_Mannual = st.selectbox(
                             'Transmission Type',
                             ('Manual Car', 'Automatic Car'))
        
    
    
    # code for Prediction
    
    
    # creating a button for Prediction
    prediction_text = ''
    
    if st.button('Calculate Price Estimate'):
        Year=2022-int(Year)
        
        
        Owner =  int(Owner)


        Present_Price =  float(Present_Price)
        Kms_Driven =  int(Kms_Driven)
        Kms_Driven2 = np.log(Kms_Driven)

        Fuel_Type_Diesel=0

        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0


    
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	

        
        if(Transmission_Mannual=='Manual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        
        prediction_text = car_model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction_text[0],2)
        
        if (output < 0):

          prediction_text = "You Cannot Sell The Car "
          
        else:
          prediction_text = "You Can Sell The Car at {}".format(output)
        
    st.success(prediction_text)


if (selected == 'House Price Prediction'):
    
    # page title
    st.title('Model is being built , will be Deployed Soon')


    st.text('Thank you for your Patience')