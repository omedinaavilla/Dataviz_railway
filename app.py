import streamlit as st
from streamlit_option_menu import option_menu



st.set_page_config(page_title="Dashboard Interactivo", layout="wide")
with st.sidebar:
    selected = option_menu("Menú", ["Contexto", "EDA", "Mapa"],
        icons=["info-circle", "bar-chart", "map"], menu_icon="cast", default_index=0)

if selected == "Contexto":
    st.title("Bienvenido al Dashboard de Turismo")
    st.markdown("""
Este dashboard interactivo presenta un análisis temático del **turismo internacional en Colombia**, 
basado en datos departamentales. Su objetivo es ofrecer una visualización clara y dinámica del comportamiento 
de esta actividad a través de distintas regiones del país.

Se incluyen **visualizaciones descriptivas** que permiten explorar el valor asignado al turismo por categoría, 
comparar promedios entre departamentos y visualizar la distribución de los datos mediante gráficos interactivos.  
Además, se incorpora una sección de **georreferenciación** que permite observar los datos en un mapa dinámico, 
usando coordenadas geográficas (latitud y longitud) para representar espacialmente los indicadores.

La base de datos utilizada proviene de un archivo `.csv` y contiene columnas como `Departamento`, `Latitud`, 
`Longitud`, `Categoría` y `Valor`, lo cual permite un enfoque tanto estadístico como geográfico del fenómeno turístico.

""")


    st.image("img/flight.png", caption="Turismo internacional",use_container_width=True)

elif selected == "EDA":
    exec(open("pages/1_Analisis.py").read())

elif selected == "Mapa":
    exec(open("pages/2_Mapa.py").read())
