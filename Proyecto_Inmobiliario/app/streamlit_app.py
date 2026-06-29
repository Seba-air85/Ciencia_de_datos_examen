import streamlit as st
import requests

st.set_page_config(
    page_title="Predicción de Viviendas",
    page_icon="🏠",
    layout="centered"
)

st.title("Predicción de Precio de Viviendas")

st.markdown("""
Ingrese las características de la propiedad y el modelo de Machine Learning
estimará su precio de venta.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    comuna = st.selectbox(
        "Comuna",
        [
            "Maipu",
            "Santiago",
            "Las Condes",
            "Providencia",
            "Puente Alto",
            "Ñuñoa"
        ]
    )

    dorms = st.number_input(
        "Dormitorios",
        min_value=1,
        value=3
    )

    baths = st.number_input(
        "Baños",
        min_value=1,
        value=2
    )

with col2:

    built_area = st.number_input(
        "Superficie construida (m²)",
        min_value=1,
        value=120
    )

    total_area = st.number_input(
        "Superficie total (m²)",
        min_value=1,
        value=180
    )

    parking = st.number_input(
        "Estacionamientos",
        min_value=0,
        value=2
    )

pobreza = st.slider(
    "Porcentaje de pobreza",
    min_value=0.00,
    max_value=0.20,
    value=0.03,
    step=0.001
)

st.divider()

if st.button("🔍 Estimar precio", use_container_width=True):

    datos = {
        "Comuna": comuna,
        "Dorms": dorms,
        "Baths": baths,
        "Built Area": built_area,
        "Total Area": total_area,
        "Parking": parking,
        "Porcentaje de personas en situación de pobreza por ingresos 2022": pobreza
    }

    with st.spinner("Calculando precio..."):

        respuesta = requests.post(
            "http://127.0.0.1:5000/predict",
            json=datos
        )

    if respuesta.status_code == 200:

        resultado = respuesta.json()

        st.success("Predicción realizada correctamente.")

        st.metric(
            label="💰 Precio estimado",
            value=f"${resultado['precio_estimado']:,.0f} CLP"
        )

    else:

        st.error("No fue posible conectarse con la API.")