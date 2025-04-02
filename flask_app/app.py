from flask import Flask, render_template, request
from weather_api import get_weather
import pandas as pd

app = Flask(__name__)
app.config['TEMPLATES_FOLDER'] = 'templates'

@app.route('/')
def home():
    print("\n=== Diagnóstico de Template ===")
    print("1. Intentando renderizar index.html...")
    try:
        result = render_template('index.html', title="Inicio")
        print("2. Template renderizado exitosamente")
        return result
    except Exception as e:
        print(f"¡Error al renderizar template!: {str(e)}")
        return "Error al cargar el template"

@app.route('/tiempo')
def tiempo():
    print("\n=== Diagnóstico de Template Tiempo ===")
    print("1. Intentando renderizar tiempo.html...")
    try:
        result = render_template('tiempo.html', title="Tiempo")
        print("2. Template renderizado exitosamente")
        return result
    except Exception as e:
        print(f"¡Error al renderizar template!: {str(e)}")
        return "Error al cargar el template"

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