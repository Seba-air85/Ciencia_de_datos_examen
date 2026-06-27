import pandas as pd


def perfil_dataset(df: pd.DataFrame, nombre: str):
    """
    Muestra información básica sobre un DataFrame.
    """

    print("\n" + "=" * 60)
    print(f"PERFIL DEL DATASET: {nombre}")
    print("=" * 60)

    print(f"\nFilas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

    print("\nTipos de datos")
    print(df.dtypes)

    print("\nValores nulos")
    print(df.isnull().sum())

    print("\nDuplicados")
    print(df.duplicated().sum())

    print("\nPrimeras 5 filas")
    print(df.head())

    