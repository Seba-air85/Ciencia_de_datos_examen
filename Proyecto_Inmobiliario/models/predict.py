import joblib
import pandas as pd

modelo = joblib.load("models/modelo/modelo_precio.pkl")
columnas = joblib.load("models/modelo/columnas.pkl")

print("Modelo cargado correctamente.")


nueva_propiedad = pd.DataFrame({
    "Comuna": ["Maipú"],
    "Dorms": [3],
    "Baths": [2],
    "Built Area": [120],
    "Total Area": [180],
    "Parking": [2],
    "Porcentaje de personas en situación de pobreza por ingresos 2022": [0.0325]
})

nueva_propiedad = pd.get_dummies(
    nueva_propiedad,
    columns=["Comuna"],
    drop_first=True
)

nueva_propiedad = nueva_propiedad.reindex(
    columns=columnas,
    fill_value=0
)

prediccion = modelo.predict(nueva_propiedad)

print(f"Precio estimado: ${prediccion[0]:,.0f} CLP")