import pandas as pd
from sqlalchemy import create_engine

# Cargar archivo CSV
df = pd.read_csv("Datos.csv")  # Aquí cambiamos a leer un CSV
print("Primeros registros del archivo:")
print(df.head())

# Configuración de conexión
usuario = "postgres"
contraseña = "clave123"  
host = "localhost"
puerto = "5432"
base_datos = "proyecto_personal"

# Crear el motor de conexión
engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

# Insertar datos en PostgreSQL
df.to_sql("datos_csv", engine, if_exists="replace", index=False)
print("\nDatos insertados correctamente en la tabla 'datos_csv'.")
