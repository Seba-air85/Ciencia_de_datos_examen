import sqlite3
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

conexion = sqlite3.connect("database/inmobiliaria.db")

df = pd.read_sql("SELECT * FROM propiedades", conexion)

conexion.close()

print(df.head())
print(df.shape)

columnas = [
    "Comuna",
    "Dorms",
    "Baths",
    "Built Area",
    "Total Area",
    "Parking",
    "Porcentaje de personas en situación de pobreza por ingresos 2022",
    "Price_CLP"
]

df = df[columnas]

print(df.head())

print(df.columns.tolist())

print("\nValores nulos:")
print(df.isnull().sum())

df = df.dropna()

print(df.shape)

X = df.drop(columns=["Price_CLP"])

y = df["Price_CLP"]

X = pd.get_dummies(
    X,
    columns=["Comuna"],
    drop_first=True
)

columnas_modelo = X.columns

print(X.head())


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)


modelo = LinearRegression()

modelo.fit(X_train, y_train)

print("Modelo entrenado correctamente.")

predicciones = modelo.predict(X_test)

mae = mean_absolute_error(y_test, predicciones)
rmse = mean_squared_error(y_test, predicciones) ** 0.5
r2 = r2_score(y_test, predicciones)

print(f"MAE: {mae:,.2f}")
print(f"RMSE: {rmse:,.2f}")
print(f"R²: {r2:.4f}")

os.makedirs("models/modelo", exist_ok=True)

joblib.dump(modelo, "models/modelo/modelo_precio.pkl")

joblib.dump(columnas_modelo, "models/modelo/columnas.pkl")

print("Modelo guardado correctamente.")

print("\n===== MÉTRICAS DEL MODELO =====")
print(f"MAE : {mae:,.2f}")
print(f"RMSE: {rmse:,.2f}")
print(f"R²  : {r2:.4f}")

print("\nModelo entrenado y guardado correctamente.")