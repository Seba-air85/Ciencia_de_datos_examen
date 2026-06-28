from extract import cargar_datasets
from transform import (
    limpiar_propiedades,
    limpiar_pobreza,
    normalizar_comunas,
    unir_datasets,
    comparar_comunas,
    perfil_dataset,
)
import os
from load import guardar_sqlite

# Extraer datos
casas_marzo, casas_julio, pobreza = cargar_datasets()
print("\n=== REGIONES DEL DATASET ORIGINAL ===")
print(pobreza["Región"].unique())

# Transformar
casas_marzo = limpiar_propiedades(casas_marzo)
casas_julio = limpiar_propiedades(casas_julio)

casas_marzo = normalizar_comunas(casas_marzo)
casas_julio = normalizar_comunas(casas_julio)
print(pobreza["Región"].unique())

pobreza = limpiar_pobreza(pobreza)

# Unir datasets de propiedades
casas = unir_datasets(casas_marzo, casas_julio)

# Verificar comunas
comparar_comunas(casas, pobreza)

print("\nComunas en casas:")
print(sorted(casas["Comuna"].unique())[:10])

print("\nComunas en pobreza:")
print(sorted(pobreza["Nombre comuna"].unique())[:10])

print("\nColumnas de pobreza:")
print(pobreza.columns.tolist())

# Merge final
dataset_final = casas.merge(
    pobreza,
    left_on="Comuna",
    right_on="Nombre comuna",
    how="left"
)

print(dataset_final[
    ["Comuna", "Nombre comuna", "Porcentaje de personas en situación de pobreza por ingresos 2022"]
].head(20))

# Revisar resultado
perfil_dataset(dataset_final, "Dataset Final")

os.makedirs("data/processed", exist_ok=True)

dataset_final.to_csv(
    "data/processed/dataset_final.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nDataset guardado correctamente.")

guardar_sqlite(dataset_final)