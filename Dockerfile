# Imagen base
FROM python:3.10

# Directorio de trabajo
WORKDIR /app

# Copiar todos los archivos del proyecto
COPY . .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto usado por Streamlit
EXPOSE 8501

# Comando para correr el dashboard de Mongo
CMD ["streamlit", "run", "dashboard_mongo.py", "--server.port=8501", "--server.address=0.0.0.0"]