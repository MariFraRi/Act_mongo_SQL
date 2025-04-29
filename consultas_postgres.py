import pandas as pd
from sqlalchemy import create_engine

# 1. Configuración de conexión a PostgreSQL
usuario = "postgres"
contraseña = "clave123"
host = "localhost"
puerto = "5432"
base_datos = "proyecto_personal"

# 2. Crear el motor de conexión
engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

print("Conectado a PostgreSQL\n")

# 3. Consultas

# 3.1 Total de registros
total = pd.read_sql('SELECT COUNT(*) FROM datos_csv', engine)
print(f"Total de registros: {total.iloc[0,0]}")

# 3.2 Conteo de registros por DEPARTAMENTO
print("\nConteo de registros por DEPARTAMENTO:")
conteo_departamento = pd.read_sql('''
    SELECT "DEPARTAMENTO", COUNT(*) as cantidad 
    FROM datos_csv 
    GROUP BY "DEPARTAMENTO"
    ORDER BY cantidad DESC
''', engine)
print(conteo_departamento)

# 3.3 Filtrar proyectos con AVANCE FÍSICO ACTUAL = 100
print("\nProyectos con AVANCE FÍSICO ACTUAL = 100:")
proyectos_terminados = pd.read_sql('''
    SELECT * 
    FROM datos_csv 
    WHERE "AVANCE FÍSICO ACTUAL" = 100
''', engine)
print(proyectos_terminados.head())  # Mostramos solo los primeros 5 para no saturar

# 3.4 Top 5 DESTINOS más frecuentes
print("\nTop 5 DESTINO más frecuentes:")
top5_destinos = pd.read_sql('''
    SELECT "DESTINO", COUNT(*) as cantidad
    FROM datos_csv
    GROUP BY "DESTINO"
    ORDER BY cantidad DESC
    LIMIT 5
''', engine)
print(top5_destinos)
