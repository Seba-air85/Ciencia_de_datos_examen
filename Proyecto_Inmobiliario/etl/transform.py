import pandas as pd

def limpiar_propiedades(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia un dataset de propiedades.
    """

    print("\nIniciando limpieza del dataset...")

    # 1. Eliminar duplicados
    df = df.drop_duplicates()

    # 2. Eliminar espacios al inicio y final
    df["Comuna"] = df["Comuna"].str.strip()
    df["Ubicacion"] = df["Ubicacion"].str.strip()

    # 3. Estandarizar nombres de comunas
    df["Comuna"] = df["Comuna"].str.title()

    # 4. Convertir columnas numéricas
    columnas_numericas = [
        "Price_CLP",
        "Price_UF",
        "Price_USD",
        "Dorms",
        "Baths",
        "Built Area",
        "Total Area",
        "Parking",
    ]

    for columna in columnas_numericas:
        df[columna] = pd.to_numeric(df[columna], errors="coerce")

    print("Limpieza terminada.")

    return df

def mostrar_comunas(df, nombre):

    if "Comuna" not in df.columns:
        return

    print("\n" + "="*60)
    print(f"COMUNAS - {nombre}")
    print("="*60)

    comunas = sorted(df["Comuna"].dropna().unique())

    for comuna in comunas:
        print(comuna)

def perfil_dataset(df: pd.DataFrame, nombre: str):

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

    # Solo si existe la columna Comuna
    if "Comuna" in df.columns:

        print("\nNúmero de comunas distintas:")
        print(df["Comuna"].nunique())

        print("\nPrimeras comunas:")
        print(sorted(df["Comuna"].dropna().unique())[:20]) 


def unir_datasets(df1, df2):

    df = pd.concat([df1, df2], ignore_index=True)

    print(f"\nTotal de registros: {len(df)}")

    print(f"Duplicados: {df.duplicated().sum()}")

    return df

def limpiar_pobreza(df):

    print("\nLimpiando dataset de pobreza...")

    df = df[df["Región"] == "Metropolitana de Santiago"]

    # Eliminar filas sin comuna
    df = df.dropna(subset=["Nombre comuna"])

    # Eliminar espacios
    df["Nombre comuna"] = df["Nombre comuna"].str.strip()

    # Estandarizar formato
    df["Nombre comuna"] = df["Nombre comuna"].str.title()

    # Aplicar los mismos reemplazos que al dataset de propiedades
    df["Nombre comuna"] = normalizar_nombres_comunas(df["Nombre comuna"])

    return df

def comparar_comunas(casas, pobreza):

    comunas_casas = set(casas["Comuna"])

    comunas_pobreza = set(pobreza["Nombre comuna"])

    print("\nSolo en Casas")

    print(sorted(comunas_casas - comunas_pobreza))

    print("\nSolo en Pobreza")

    print(sorted(comunas_pobreza - comunas_casas))

def normalizar_nombres_comunas(serie):
    reemplazos = {
        "Caleradetango": "Calera de Tango",
        "Cerronavia": "Cerro Navia",
        "Elbosque": "El Bosque",
        "Elmonte": "El Monte",
        "Estacióncentral": "Estación Central",
        "Islademaipo": "Isla de Maipo",
        "Lacisterna": "La Cisterna",
        "Laflorida": "La Florida",
        "Lagranja": "La Granja",
        "Lapintana": "La Pintana",
        "Lareina": "La Reina",
        "Lascondes": "Las Condes",
        "Lobarnechea": "Lo Barnechea",
        "Loespejo": "Lo Espejo",
        "Loprado": "Lo Prado",
        "Padrehurtado": "Padre Hurtado",
        "Pedroaguirrecerda": "Pedro Aguirre Cerda",
        "Puentealto": "Puente Alto",
        "Quintanormal": "Quinta Normal",
        "Sanbernardo": "San Bernardo",
        "Sanjoaquín": "San Joaquín",
        "Sanjosédemaipo": "San José de Maipo",
        "Sanmiguel": "San Miguel",
        "Sanpedro": "San Pedro",
        "Sanramón": "San Ramón",
        "Maríapinto": "María Pinto",
        "María Pinto": "María Pinto",
        "Calera De Tango": "Calera de Tango",
        "Isla De Maipo": "Isla de Maipo",
        "San José De Maipo": "San José de Maipo"
    }

    return serie.replace(reemplazos)

def normalizar_comunas(df):

    df["Comuna"] = normalizar_nombres_comunas(df["Comuna"])

    return df