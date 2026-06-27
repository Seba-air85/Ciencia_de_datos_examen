from extract import cargar_datasets

casas_marzo, casas_julio, pobreza = cargar_datasets()

print(casas_marzo.head())

print(casas_julio.head())

print(pobreza.head())