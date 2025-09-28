def limpiar_columnas_monetarias(df, columnas):
    for col in columnas:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(r'[^\d,.-]', '', regex=True)
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )
    return df