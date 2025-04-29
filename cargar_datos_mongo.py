from pymongo import MongoClient

# Conexión a MongoDB Atlas
url = "mongodb+srv://francoriatiga:marifrari12@cluster0.cckjpmh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(url)

# Base de datos y colección
db = client["proyecto_personal"]
coleccion = db["datos_csv"]

print("Conectado a MongoDB Atlas\n")

# 1. Total de registros
total = coleccion.count_documents({})
print(f"Total de registros en la colección: {total}")

# 2. Conteo de proyectos por departamento
print("\nConteo de registros por DEPARTAMENTO:")
conteo_departamento = coleccion.aggregate([
    {"$group": {"_id": "$DEPARTAMENTO", "cantidad": {"$sum": 1}}},
    {"$sort": {"cantidad": -1}}
])
for dep in conteo_departamento:
    print(dep)

# 3. Filtrar proyectos con AVANCE FÍSICO ACTUAL igual a 100
print("\nProyectos con AVANCE FÍSICO ACTUAL = 100:")
proyectos_terminados = coleccion.find({"AVANCE FÍSICO ACTUAL": 100})
for proyecto in proyectos_terminados.limit(5):  # Solo mostrar primeros 5 para no saturar
    print(proyecto)

# 4. Top 5 DESTINOS más frecuentes
print("\nTop 5 DESTINO más frecuentes:")
top5_destinos = coleccion.aggregate([
    {"$group": {"_id": "$DESTINO", "conteo": {"$sum": 1}}},
    {"$sort": {"conteo": -1}},
    {"$limit": 5}
])
for destino in top5_destinos:
    print(destino)
