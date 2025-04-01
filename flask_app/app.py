from flask import Flask, render_template, request
from weather_api import get_weather
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', titulo="Inicio")

@app.route('/tiempo')
def mostrar_formulario_tiempo():
    return render_template('tiempo.html', titulo="Consultar Tiempo")

@app.route('/obtener-tiempo', methods=['POST'])
def procesar_tiempo():
    ciudad = request.form['city']
    
    try:
        all_info = get_weather(ciudad)
        #location_df, current_df, icon = get_weather(ciudad)

        # Añadir el ícono al campo 'condition'
        # current_df['condition'] = current_df['condition'].apply(
        #     lambda x: f"<img src='{icon}' style='width: 30px; height: 30px;'/>"
        # )
        
        # Convertir el DataFrame Location a HTML para mostrarlo
        table1_html = all_info[0].to_html(
            classes='table table-striped', 
            index=False,
            escape=False  # Esto permite que el HTML en las celdas se renderice
        )

        # Convertir el DataFrame Current a HTML para mostrarlo
        table2_html = all_info[1].to_html(
            classes='table table-striped', 
            index=False,
            escape=False  # Esto permite que el HTML en las celdas se renderice
        )

        humidity_value = all_info[6]['humidity'].values[0]
        dewpoint_value = all_info[6]['dewpoint_c'].values[0]

        
        return render_template(
            'tiempo.html',
            titulo="Resultado del Tiempo",
            resultado1=table1_html,
            resultado2=table2_html,
            humidity=humidity_value,
            dewpoint=dewpoint_value,
            ciudad=ciudad
        )
    except Exception as e:
        error_msg = f"Error al obtener datos para {ciudad}: {str(e)}"
        return render_template(
            'tiempo.html',
            titulo="Error",
            error=error_msg
        )

if __name__ == '__main__':
    app.run(debug=True)