import streamlit as st
import pandas as pd 

opcion = st.sidebar.selectbox(
    "selecciona una opción",
    ["Vehículos"]

)

vehiculos = pd.read_csv("Electric_Vehicle_Population.csv")

if opcion == "Vehículos":
    st.title("Análisis de Vehículos Eléctricos")

    st.subheader("Dimensiones del dataset")
    st.write(vehiculos.shape)

    st.subheader("Columnas")
    st.write(vehiculos.columns.tolist())

    st.subheader("Primeras 6 filas")
    st.dataframe(vehiculos.head(6))

    st.subheader("Estadísticas")
    st.write(vehiculos.describe())

    st.subheader("Modelo de carro")

    year = st.number_input(
        "Mostrar vehículos con año menor a:",
        min_value=2000,
        max_value=2025
    )

    yearfiltro = vehiculos[vehiculos["Model Year"] < year]


    st.write(yearfiltro)

    st.subheader("Por precio")

    precio = st.number_input(

        "Mostrar vihículos con precio menor a:",
        min_value=0.0,
        max_value=845000.0
    )

    filtro_porprecio = vehiculos[vehiculos["Base_MSRP"] < precio]

    st.write(filtro_porprecio)

    def clasificar_rango(x):
        if x < 100:
            return "Bajo"

        elif x <= 250:
            return "Medio"
        
        else:
            return "Alto"


    vehiculos["RangoCategoria"] = vehiculos["Electric_Range"].apply(clasificar_rango)

    st.subheader("Nueva columna")

    st.write(vehiculos[["Electric_Range", "RangoCategoria"]].head(10))

    st.subheader("Conteo por categoría")

    conteo = vehiculos["RangoCategoria"].value_counts()

    st.write(conteo)

    st.subheader("Gráfico de categorías")

    st.bar_chart(conteo)

    st.subheader("Análisis agrupado")

    grupo = vehiculos.groupby("RangoCategoria").agg({
        "Base_MSRP": "mean",
        "Model Year": "mean",
        "Electric_Range": "std"

    })
        
    st.write(grupo)

