import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Caracteristicas de los autos listados')

st.write('Esta aplicación aún no es funcional. En construcción.')
        
car_data = pd.read_csv('vehicles_us.csv') 
hist_button = st.button('Constuye un histograma') 
        
if hist_button: 
            
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.histogram(car_data, x="odometer", labels={"odometer": "odómetro"})

    st.plotly_chart(fig, use_container_width=True)

    import streamlit as st

build_histogram = st.checkbox('Da click si ya terminaste')

if build_histogram:
    st.write('Construiste un histograma para la columna odómetro')  

