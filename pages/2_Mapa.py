import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium



# Cargar datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv("turismo_internacional.csv")
    return df

df = cargar_datos()

st.title("Mapa Interactivo por Departamento")

# Validar columnas necesarias
if all(col in df.columns for col in ["Departamento", "Latitud", "Longitud", "Valor", "Categoría"]):

    st.subheader("Filtrado por Categoría")
    categorias = df["Categoría"].unique()
    seleccionadas = st.multiselect("Selecciona una o más categorías", categorias, default=categorias)

    df_filtrado = df[df["Categoría"].isin(seleccionadas)]

    # Crear mapa centrado en Colombia
    mapa = folium.Map(location=[4.5709, -74.2973], zoom_start=5, tiles="CartoDB positron")

    # Añadir marcadores
    for _, row in df_filtrado.iterrows():
        folium.CircleMarker(
            location=[row["Latitud"], row["Longitud"]],
            radius=row["Valor"] * 10,  # puedes ajustar este multiplicador
            popup=f"{row['Departamento']}<br>Valor: {row['Valor']:.2f}<br>Categoría: {row['Categoría']}",
            color="blue",
            fill=True,
            fill_opacity=0.6
        ).add_to(mapa)

    st_folium(mapa, width=1000, height=600)

else:
    st.warning("Faltan columnas necesarias: Departamento, Latitud, Longitud, Valor, Categoría.")
