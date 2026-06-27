import pandas as pd
from config import RAW_DATA


def cargar_datasets():

    casas_marzo = pd.read_csv(
        RAW_DATA / "2023-03-08 Precios Casas RM.csv"
    )

    casas_julio = pd.read_csv(
        RAW_DATA / "2023-07-18 Propiedades Web Scrape.csv"
    )

    pobreza = pd.read_excel(
        RAW_DATA / "estimaciones_tasa_pobreza_ingresos_comunas_2022.xlsx",
        header=2
    )

    return casas_marzo, casas_julio, pobreza