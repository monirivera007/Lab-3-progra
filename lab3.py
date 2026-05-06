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

videojuegos = pd.read_csv("steam_store_data_2024.csv")

videojuegos["price"] = videojuegos["price"].str.replace("$", "", regex=False)

videojuegos["price"] = pd.to_numeric(videojuegos["price"], errors="coerce")

videojuegos = videojuegos.dropna(subset=["price"])

videojuegos["salePercentage"] = videojuegos["salePercentage"].str.replace("%", "", regex=False)

videojuegos["salePercentage"] = pd.to_numeric(videojuegos["salePercentage"], errors="coerce")

videojuegos = videojuegos.dropna(subset=["salePercentage"])

if opcion == "Videojuegos":

    st.title("Análisis de Videojuegos")
    
    st.subheader("Dimensiones del dataset")
    st.write(videojuegos.shape)

    st.subheader("Columnas")
    st.write(videojuegos.columns.tolist())

    st.subheader("Primeras 6 filas")
    st.dataframe(videojuegos.head(6))

    st.subheader("Estadísticas")
    st.write(videojuegos.describe())

    st.subheader("Filtro por precio")

    precio = st.number_input("Precio mayor a:", min_value=0.0)

    filtro_precio = videojuegos[videojuegos["price"] > precio]

    st.write(filtro_precio)

    st.subheader("Filtro por descuento")

    descuento = st.number_input("Descuento menor a:", min_value=0.0)

    filtro_descuento = videojuegos[videojuegos["salePercentage"] < descuento]

    st.write(filtro_descuento)

    def gama_juego(x):
        if x < 10:
            return "Baja"
        elif x <= 24:
            return "Media"
        else:
            return "Alta"

    videojuegos["GamaJuego"] = videojuegos["price"].apply(gama_juego)

    st.subheader("Conteo por gama")

    conteo = videojuegos["GamaJuego"].value_counts()

    st.write(conteo)

    st.bar_chart(conteo)

    st.subheader("Análisis agrupado")

    grupo = videojuegos.groupby("GamaJuego").agg({
        "price": ["mean", "std"],
        "salePercentage": "mean",
    
    })

    st.write(grupo)

    st.subheader("Calificación por gama")

    reviews = videojuegos.groupby("GamaJuego")["allReviews"].value_counts()

    st.write(reviews)

    videojuegos.to_csv("steam_store_data_2024_Actualizado.csv", index=False)




elif opcion == "Netflix":
    st.title("Análisis Netflix")
    
  
    netflix = pd.read_csv("netflix_titles.csv")
    
    
    def tipo_audiencia(rating):
        if rating in ["G", "TV-Y", "TV-G", "TV-Y7", "TV-Y7-FV"]:
            return "Niños"
        elif rating in ["PG", "TV-PG"]:
            return "Adolescentes"
        elif rating in ["PG-13", "TV-14"]:
            return "Adultos Jóvenes"
        elif rating in ["R", "TV-MA", "NC-17"]:
            return "Adultos"
        else:
            return "No clasificado"
    
    netflix["TipoAudiencia"] = netflix["rating"].apply(tipo_audiencia)
    
    # Vista general
    col1, col2 = st.columns(2)
    col1.metric("Total títulos", netflix.shape[0])
    col2.metric("Columnas", len(netflix.columns))
    
    st.subheader("Primeras 6 filas")
    st.dataframe(netflix.head(6))
    
    
    st.subheader("Filtros")
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        
        st.markdown("**Duración > minutos**")
        duracion_min = st.number_input("Películas con duración mayor a:", 
                                     min_value=0, value=60, step=10)
        
       
        def extraer_minutos(duracion):
            if pd.isna(duracion):
                return 0
            dur_str = str(duracion)
            if "min" in dur_str:
                try:
                    return int(dur_str.split(" ")[0])
                except:
                    return 0
            return 0
        
        netflix["duracion_min"] = netflix["duration"].apply(extraer_minutos)
        
        
        peliculas_largas = netflix[
            (netflix["type"] == "Movie") & 
            (netflix["duracion_min"] > duracion_min)
        ]
        
        if not peliculas_largas.empty:
            st.success(f" {len(peliculas_largas)} películas encontradas")
            st.dataframe(peliculas_largas[["title", "duration", "duracion_min", "TipoAudiencia"]].head())
        else:
            st.warning("No se encontraron películas con esa duración")
    
    with col_f2:
       
        st.markdown("**Añadido antes del año**")
        anio_maximo = st.number_input("Contenido añadido antes del:", 
                                    min_value=2008, max_value=2026, value=2020)
        
        
        def extraer_anio(fecha):
            if pd.isna(fecha):
                return 2000
            fecha_str = str(fecha)
            try:
                
                for i in range(len(fecha_str)-3, 0, -1):
                    if fecha_str[i:i+4].isdigit():
                        return int(fecha_str[i:i+4])
                return 2000
            except:
                return 2000
        
        netflix["anio_agregado"] = netflix["date_added"].apply(extraer_anio)
        contenido_viejo = netflix[netflix["anio_agregado"] < anio_maximo]
        
        if not contenido_viejo.empty:
            st.success(f"{len(contenido_viejo)} contenidos encontrados")
            st.dataframe(contenido_viejo[["title", "date_added", "anio_agregado", "TipoAudiencia"]].head())
        else:
            st.warning("No se encontró contenido de ese periodo")
    
   
    st.subheader("👥 Distribución por Audiencia")
    conteo_audiencia = netflix["TipoAudiencia"].value_counts()
    st.bar_chart(conteo_audiencia)
    
   
    # Tabla resumen SIN lambda
st.subheader(" Resumen por Audiencia")
resumen = netflix.groupby("TipoAudiencia").agg({
    "title": "count"
}).rename(columns={"title": "Total"})


peliculas_por_audiencia = {}
for audiencia in netflix["TipoAudiencia"].unique():
    count_peliculas = len(netflix[(netflix["TipoAudiencia"] == audiencia) & (netflix["type"] == "Movie")])
    peliculas_por_audiencia[audiencia] = count_peliculas  # ← "audiencia" en minúscula


resumen["Películas"] = [peliculas_por_audiencia.get(audiencia, 0) for audiencia in resumen.index]
st.dataframe(resumen)