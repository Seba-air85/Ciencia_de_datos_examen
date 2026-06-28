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

# Transformar
casas_marzo = limpiar_propiedades(casas_marzo)
casas_julio = limpiar_propiedades(casas_julio)

casas_marzo = normalizar_comunas(casas_marzo)
casas_julio = normalizar_comunas(casas_julio)

pobreza = limpiar_pobreza(pobreza)

# Unir datasets de propiedades
casas = unir_datasets(casas_marzo, casas_julio)

# Verificar comunas
comparar_comunas(casas, pobreza)

# Merge final
dataset_final = casas.merge(
    pobreza,
    left_on="Comuna",
    right_on="Nombre comuna",
    how="left"
)

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