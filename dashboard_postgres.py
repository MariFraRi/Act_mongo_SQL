import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# 1. Conexión a PostgreSQL
usuario = "postgres"
contraseña = "clave123"
host = "localhost"
puerto = "5432"
base_datos = "proyecto_personal"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

st.title("📊 Dashboard de Proyectos (PostgreSQL vía SQL Directo)")

# --- DIVIDIR EN COLUMNAS ---
col1, col2 = st.columns(2)

# 2. Gráfico 1: Proyectos por Departamento (consulta SQL)
with col1:
    st.subheader("Proyectos por Departamento")
    query1 = '''
        SELECT "DEPARTAMENTO", COUNT(*) AS cantidad
        FROM datos_csv
        GROUP BY "DEPARTAMENTO"
        ORDER BY cantidad DESC
    '''
    conteo_departamento = pd.read_sql(query1, engine)
    fig1 = px.bar(conteo_departamento, x='DEPARTAMENTO', y='cantidad', labels={'DEPARTAMENTO': 'Departamento', 'cantidad': 'Cantidad'})
    st.plotly_chart(fig1, use_container_width=True)

# 3. Gráfico 2: Avance Físico Promedio por Departamento (consulta SQL)
with col2:
    st.subheader("Avance Físico Promedio")
    query2 = '''
        SELECT "DEPARTAMENTO", AVG("AVANCE FÍSICO ACTUAL") AS promedio_avance
        FROM datos_csv
        GROUP BY "DEPARTAMENTO"
        ORDER BY promedio_avance DESC
    '''
    avance_departamento = pd.read_sql(query2, engine)
    fig2 = px.bar(avance_departamento, x='DEPARTAMENTO', y='promedio_avance', labels={'DEPARTAMENTO': 'Departamento', 'promedio_avance': 'Promedio Avance (%)'})
    st.plotly_chart(fig2, use_container_width=True)

# --- GRÁFICO ABAJO ---
st.subheader("Top 5 DESTINOS más frecuentes")
query3 = '''
    SELECT "DESTINO", COUNT(*) AS cantidad
    FROM datos_csv
    GROUP BY "DESTINO"
    ORDER BY cantidad DESC
    LIMIT 5
'''
top5_destinos = pd.read_sql(query3, engine)
fig3 = px.pie(top5_destinos, names='DESTINO', values='cantidad', title="Top 5 DESTINOS")
st.plotly_chart(fig3, use_container_width=True)
