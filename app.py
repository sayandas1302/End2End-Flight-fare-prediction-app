# this python file is to develop a web app for the flight-fare predictions
import streamlit as st
import pandas as pd
import numpy as np
import artifacts
import pickle

# The functionality behind the app

# function to show the result on button click
def show_result():
    with resultbox:
        with col2:
            st.write(f'## Rs. {predict(X_inserted)}')

def predict(x):
    with open('model.pkl',"rb") as f:
        loaded_model=pickle.load(f)
    return round(loaded_model.predict(x)[0],2)

# The Layout of the app

# background
st.markdown(f"""
         <style>
         .stApp {{
             background-image: url("https://live.staticflickr.com/6083/6153002630_fd390b6276_b.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """, unsafe_allow_html=True)

# app title
st.write('''
## Flight Fare Prediction App
This app takes input from the user and Predict The flight fare on basis of that information
''')

# container for input
with st.container():
    st.subheader('Insert your specification')
    col1, col2= st.columns(2)

    with col1:
        src=st.selectbox('Source: ',options=artifacts.source_names+["Bangalore"])
        dest=st.selectbox('Destination: ',options=[name for name in artifacts.destination_names+["Bangalore"] if name!=src])
        airline=st.selectbox('Airline Service: ',options=artifacts.airline_names+["Air Asia"])   

    with col2:
        dept_time=st.time_input('Departure Time: ')
        arr_time=st.time_input('Arrival Time: ')
        jrny_dt=st.date_input('Journey Date')
    
    stop=st.radio('Stopage: ',
                   options=["no-stop","1 stop","2 stop","3 stop","4 stop"],
                   index=1,horizontal=True)   

# processing for the input
total_stop=int(stop.split(" ")[0]) if " " in stop else 0

jrny_day=jrny_dt.day
jrny_month=jrny_dt.month

dept_hour=dept_time.hour
dept_minute=dept_time.minute

arr_hour=arr_time.hour
arr_minute=arr_time.minute

dur_hr=arr_hour-dept_hour
dur_min=arr_minute-dept_minute

airline_dummies=np.zeros(len(artifacts.airline_names))
if airline in artifacts.airline_names:
    indx=artifacts.airline_names.index(airline)
    airline_dummies[indx]=1

source_dummies=np.zeros(len(artifacts.source_names))
if src in artifacts.source_names:
    indx=artifacts.source_names.index(src)
    source_dummies[indx]=1

dest_dummies=np.zeros(len(artifacts.destination_names))
if dest in artifacts.destination_names:
    indx=artifacts.destination_names.index(dest)
    dest_dummies[indx]=1

x=[total_stop,jrny_day,jrny_month,
   dept_hour,dept_minute,arr_hour,arr_minute,
   dur_hr,dur_min]+list(airline_dummies)+list(source_dummies)+list(dest_dummies)

X_inserted=pd.DataFrame([x])

# container for button
with st.container():
    col1, col2, col3 , col4, col5=st.columns(5)
    
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        center_button = st.button('I\'m Done!',on_click=show_result)

# container for result
resultbox=st.container()

with resultbox:
    col1,col2,col3=st.columns(3)

    with col1:
        st.write('## Fare:')
