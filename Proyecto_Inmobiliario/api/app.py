from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

modelo = joblib.load("models/modelo/modelo_precio.pkl")
columnas = joblib.load("models/modelo/columnas.pkl")

print("Modelo cargado correctamente.")

@app.route("/")
def inicio():
    return "API funcionando correctamente"


@app.route("/predict", methods=["POST"])
def predict():

    datos = request.get_json()

    nueva_propiedad = pd.DataFrame([datos])

    nueva_propiedad = pd.get_dummies(
        nueva_propiedad,
        columns=["Comuna"],
        drop_first=True
    )

    nueva_propiedad = nueva_propiedad.reindex(
        columns=columnas,
        fill_value=0
    )

    precio = modelo.predict(nueva_propiedad)[0]

    return jsonify({
    "precio_estimado": int(precio)
    })

if __name__ == "__main__":
    app.run(debug=True)