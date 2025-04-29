import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient

# 1. Conexión a MongoDB
url = "mongodb+srv://francoriatiga:marifrari12@cluster0.cckjpmh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(url, tlsAllowInvalidCertificates=True)
db = client["proyecto_personal"]
coleccion = db["datos_csv"]

st.title("📊 Dashboard de Proyectos (MongoDB vía consultas)")

# --- DIVIDIR EN COLUMNAS ---
col1, col2 = st.columns(2)

# 2. Gráfico 1: Proyectos por Departamento (consulta MongoDB)
with col1:
    st.subheader("Proyectos por Departamento")
    conteo_departamento = list(coleccion.aggregate([
        {"$group": {"_id": "$DEPARTAMENTO", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]))
    df_conteo = pd.DataFrame(conteo_departamento)
    df_conteo.rename(columns={"_id": "DEPARTAMENTO"}, inplace=True)
    fig1 = px.bar(df_conteo, x='DEPARTAMENTO', y='count', labels={'DEPARTAMENTO':'Departamento', 'count':'Cantidad'})
    st.plotly_chart(fig1, use_container_width=True)

# 3. Gráfico 2: Avance Físico Promedio (consulta MongoDB)
with col2:
    st.subheader("Avance Físico Promedio por Departamento")
    avance_departamento = list(coleccion.aggregate([
        {"$group": {"_id": "$DEPARTAMENTO", "promedio_avance": {"$avg": "$AVANCE FÍSICO ACTUAL"}}},
        {"$sort": {"promedio_avance": -1}}
    ]))
    df_avance = pd.DataFrame(avance_departamento)
    df_avance.rename(columns={"_id": "DEPARTAMENTO"}, inplace=True)
    fig2 = px.bar(df_avance, x='DEPARTAMENTO', y='promedio_avance', labels={'DEPARTAMENTO':'Departamento', 'promedio_avance':'Promedio Avance (%)'})
    st.plotly_chart(fig2, use_container_width=True)

# --- GRÁFICO ABAJO ---
st.subheader("Top 5 DESTINOS más frecuentes")
top5_destinos = list(coleccion.aggregate([
    {"$group": {"_id": "$DESTINO", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 5}
]))
df_destinos = pd.DataFrame(top5_destinos)
df_destinos.rename(columns={"_id": "DESTINO"}, inplace=True)
fig3 = px.pie(df_destinos, names='DESTINO', values='count', title="Top 5 DESTINOS")
st.plotly_chart(fig3, use_container_width=True)
