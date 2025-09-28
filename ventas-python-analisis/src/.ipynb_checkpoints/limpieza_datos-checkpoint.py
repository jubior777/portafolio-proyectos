# limpieza_datos.py

import pandas as pd

def limpiar_importe(valor):
    """
    Convierte importes tipo '1.234,56 €' en float 1234.56
    """
    try:
        limpio = (
            str(valor)
            .strip()
            .replace('€', '')
            .replace('.', '')
            .replace(',', '.')
        )
        return float(limpio)
    except:
        return None

def limpiar_columna_importes(df, columna):
    """
    Aplica limpieza a una columna de importes en un DataFrame.
    """
    df[columna] = df[columna].apply(limpiar_importe)
    return df

def estandarizar_columnas(df):
    """
    Elimina espacios y estandariza nombres de columnas.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df