import pandas as pd

def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    df.dropna(inplace=True)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    return df

if __name__ == "__main__":
    datos = cargar_datos("../data/ventas.csv")
    print(datos.head())