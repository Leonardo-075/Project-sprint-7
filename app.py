import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Visualización de datos de anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Crear tabla de datos
st.dataframe(car_data)

# crear un botón para el histograma.
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer',
                       title='Histograma del kilometraje(millas) de los coches')
    # agregar etiquetas
    fig.update_layout(
        xaxis_title='Kilometraje (millas)',
        yaxis_title='Cantidad de coches',
        bargap=0.2,  # espacio entre barras
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")

# crear un botón para el diagrama de dispersión.
disp_button = st.button('Construir diagrama de dispersión')
if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x='model_year', y='price',
                     title='Diagrama de dispersión del modelo respecto al precio')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")
    st.write('¡Gracias por usar la aplicación!')
