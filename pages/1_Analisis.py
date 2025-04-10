import streamlit as st
import pandas as pd
import plotly.express as px




# Cargar los datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv("turismo_internacional.csv")
    return df


df = cargar_datos()

st.title("Análisis Descriptivo del Turismo")

# Mostrar la tabla
st.subheader("Datos generales")
st.dataframe(df)

# Estadísticas básicas
st.subheader("Estadísticas descriptivas de 'Valor'")
st.write(df["Valor"].describe())

# Gráfico 1: Promedio de valor por departamento
st.subheader("Promedio de Valor por Departamento")
promedios = df.groupby("Departamento")["Valor"].mean().reset_index()
fig1 = px.bar(promedios, x="Departamento", y="Valor", title="Valor promedio por departamento", color="Valor")
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Distribución de categorías
st.subheader("Distribución de Categorías")
fig2 = px.pie(df, names="Categoría", title="Participación de cada categoría")
st.plotly_chart(fig2)

# Gráfico 3: Boxplot por categoría
st.subheader("Distribución de Valor por Categoría")
fig3 = px.box(df, x="Categoría", y="Valor", points="all", title="Boxplot de Valor por Categoría")
st.plotly_chart(fig3, use_container_width=True)

