import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Visualización de datos de anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer', title='Histograma del odómetro')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")

disp_button = st.button('Construir diagrama de dispersión')  # crear un botón
if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x='model_year', y='price',
                     title='Diagrama de dispersión del precio frente al año')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")
    st.write('¡Gracias por usar la aplicación!')
