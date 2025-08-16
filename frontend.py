import streamlit as st
import pandas as pd
import pickle
st.set_page_config(page_title='Car_price_prediction',page_icon='car1.png')
st.header('Welcome to Car price predictor:')
df=pd.read_csv('copied.csv')
make_comp= list(df['Make'].unique())
make_comp.sort()
car_model= list(df['Model'].unique())
car_model.sort()
Year = list(df['Year'].unique())
Year.sort()
fuel_type = list(df['Fuel Type'].unique())
fuel_type.sort()
transmission_type = list(df['Transmission'].unique())
transmission_type.sort()
with open('RFmodel.pkl','rb')as file:
    model=pickle.load(file)
with st.container(border=True):
    col1,col2=st.columns(2)
    make=col1.selectbox("Company:",options=make_comp)
    mod=col2.selectbox('Model:',options=car_model)
    year=col1.selectbox('Year:',options=Year)
    engineSize = col2.number_input("Engine Size: ",min_value=1.0,max_value=4.5)
    mileage = col1.number_input("Mileage: ",min_value=50,max_value=200000)
    fuel=col2.selectbox('Fuel Type:',options=fuel_type)
    transmission=col1.selectbox("Transmission Type: ",options=transmission_type)

    input_values=[(make_comp.index(make),car_model.index(mod),year,engineSize,mileage,fuel_type.index(fuel),transmission_type.index(transmission))]
    
    c1,c2,c3=st.columns([1.6,1.5,1])
    if c2.button("Predict Price"):
        out = model.predict(input_values)
        st.write(f"Predicted Price: {out[0]}")


    car_model= list(df['Model'].unique())
    car_model.sort()

    Year = list(df['Year'].unique())
    Year.sort()

    fuel_type = list(df['Fuel Type'].unique())
    fuel_type.sort()

    transmission_type = list(df['Transmission'].unique())
    transmission_type.sort()



