import streamlit as st
import pandas as pd 

opcion = st.sidebar.selectbox(
    "selecciona una opción",
    ["Vehículos", "Gimnasio", "Videojuegos", "Netflix"]

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

gimnasio =pd.read_csv("GymExerciseTracking.csv")

if opcion == "Gimnasio":

    st.title("Analisis de Gimnasio")

    st.subheader("Dimensiones del dataset")
    st.write(gimnasio.shape)

    st.subheader("Columnas")
    st.write(gimnasio.columns.tolist())

    st.subheader("Primeras 6 filas")
    st.dataframe(gimnasio.head(6))

    st.subheader("Estadísticas")
    st.write(gimnasio.describe())

    st.subheader("Filtro por calorías")

    calorias = st.number_input(
        "Mostrar registros con calorías >= a:",
        min_value=0.0

    )

    filtro_calorias = gimnasio[gimnasio["Calories_Burned"] >= calorias]

    st.write(filtro_calorias)
    
    st.subheader("Filtro por porcentaje de grasa")

    grasa = st.number_input(
        "mostrar registros con grasa <= a:",
        min_value=0.0,
        max_value=100.0

    )

    filtro_grasa = gimnasio[gimnasio["Fat_Percentage"] <= grasa]

    st.write(filtro_grasa)

    def nivel_frecuencia(x):
        if x < 3: 
            return "Baja"
        elif x <= 5:
            return "Moderada" 
        else:
            return "Alta"

    gimnasio["NivelFrecuencia"] = gimnasio["Workout_Frequency (days/week)"].apply(nivel_frecuencia)

    st.subheader("Conteo por frecuencia")

    conteo = gimnasio["NivelFrecuencia"].value_counts()

    st.write(conteo)

    st.subheader("Gráfico de frecuencia")

    st.bar_chart(conteo)

    st.subheader("Análisis agrupado")

    grupo = gimnasio.groupby("NivelFrecuencia").agg({
        "Session_Duration (hours)": "mean",
        "Experience_Level": "mean",
        "BMI": "std"
    })

    st.write(grupo)

    st.subheader("Relación calorías vs duración")

    correlacion = gimnasio[["Calories_Burned", "Session_Duration (hours)"]].corr()

    st.write(correlacion)

    st.subheader("Relación grasa vs experiencia")

    correlacion2 = gimnasio[["Fat_Percentage", "Experience_Level"]].corr()

    st.write(correlacion2)

    gimnasio.to_csv("GymExerciseTracking_Actualizado.csv", index=False)
