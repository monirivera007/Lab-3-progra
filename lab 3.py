import streamlit as st
import pandas as pd 

vehiculos = pd.read_csv("Electric_Vehicle_Population.csv")
st.title("Análisis de Vehículos Eléctricos")

st.subheader("Dimensiones del dataset")
st.write(vehiculos.shape)

st.subheader("Columnas")
st.write(vehiculos.columns.tolist())

st.subheader("primeras 6 filas")
st.dataframe(vehiculos.head(6))

st.subheader("Estadísticas")
st.write(vehiculos.describe())

st.subheader("Modelo de carro")

ayear = st.number_input(
    "Mostrar vehículos con año menor a:",
    year_minimo = 2000,
    year_maxiumo = 2025
)

yearfiltro = vehiculos[vehiculos["Año de modelo"] < year]

st.write(yearfiltro)