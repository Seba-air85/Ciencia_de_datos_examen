import joblib
import pandas as pd

modelo = joblib.load("models/modelo/modelo_precio.pkl")

print("Modelo cargado correctamente.")


nueva_propiedad = pd.DataFrame({
    "Dorms": [3],
    "Baths": [2],
    "Built Area": [120],
    "Total Area": [180],
    "Parking": [2],
    "Porcentaje de personas en situación de pobreza por ingresos 2022": [0.03],
    "Comuna": ["Maipú"]
})

nueva_propiedad = pd.get_dummies(
    nueva_propiedad,
    columns=["Comuna"],
    drop_first=True
)