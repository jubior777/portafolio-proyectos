from flask import Flask, render_template, request
import pandas as pd
from limpieza_inventario import limpiar_columnas_monetarias

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dashboard():
    df = pd.read_csv('../data/inventario.csv', encoding='utf-8')
    df = limpiar_columnas_monetarias(df, ['precio_unitario', 'valor_total'])
    df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'], errors='coerce')

    # Filtros desde formulario
    categoria = request.args.get('categoria')
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    if categoria:
        df = df[df['categoria'] == categoria]
    if fecha_inicio:
        df = df[df['fecha_ingreso'] >= fecha_inicio]
    if fecha_fin:
        df = df[df['fecha_ingreso'] <= fecha_fin]

    resumen = df.groupby('categoria')['valor_total'].sum().reset_index()
    categorias = df['categoria'].unique()

    return render_template('index.html', resumen=resumen.to_dict(orient='records'), categorias=categorias)

if __name__ == '__main__':
    app.run(debug=True)