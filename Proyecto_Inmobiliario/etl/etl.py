from extract import cargar_datasets
from transform import perfil_dataset

casas_marzo, casas_julio, pobreza = cargar_datasets()

perfil_dataset(casas_marzo, "Casas Marzo")
perfil_dataset(casas_julio, "Casas Julio")
perfil_dataset(pobreza, "Pobreza")

if "Comuna" in df.columns:

    print("\nNúmero de comunas distintas:")
    print(df["Comuna"].nunique())

    print("\nPrimeras comunas:")
    print(sorted(df["Comuna"].dropna().unique())[:20])