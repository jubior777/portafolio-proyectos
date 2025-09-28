import pandas as pd
import json
from limpieza_inventario import limpiar_columnas_monetarias

df = pd.read_csv('data/inventario.csv', encoding='utf-8')
df = limpiar_columnas_monetarias(df, ['precio_unitario', 'valor_total'])

resumen = df.groupby('categoria')['valor_total'].sum().reset_index()
resumen.to_json('assets/inventario.json', orient='records')
print("✅ JSON generado en assets/inventario.json")