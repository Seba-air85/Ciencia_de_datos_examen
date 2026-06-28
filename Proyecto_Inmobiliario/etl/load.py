import sqlite3
import os

def guardar_sqlite(df):

    # Crear carpeta database si no existe
    os.makedirs("database", exist_ok=True)

    # Crear la base de datos
    conexion = sqlite3.connect("database/inmobiliaria.db")

    # Guardar el DataFrame como tabla
    df.to_sql(
        "propiedades",
        conexion,
        if_exists="replace",
        index=False
    )

    conexion.close()

    print("Base de datos SQLite creada correctamente.")