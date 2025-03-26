import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

#Usando la API de AEMET, vais a tener que buscar la temperatura media que hizo en getafe entre el 22 y 23 de agosto de este año a las 10:30
#  (2024-08-22T08:30:30UTC)
#  (2024-08-23T08:30:30UTC)
def solucion():
    api_key = os.getenv("AEMET_API_KEY")
    all_stations_url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"
    
    headers = {
        'accept': 'application/json',
        'api_key': api_key,
        'cache-control': 'no-cache'
    }

    init_date_str = '2024-08-22T08:30:30UTC'
    end_date_str = '2024-08-23T08:30:30UTC'

    # Obtengo el código EMA de la Estacion de GETAFE
    response = requests.get(all_stations_url, headers=headers).json()
    data_url = response['datos']
    data = requests.get(data_url).json()
    df = pd.DataFrame(data)
    ema_code_value = df.loc[df['nombre'] == 'GETAFE', 'indicativo'].values[0]

    # Construyo la URL para obtener los datos solicitados
    encoded_init_date = init_date_str.replace(':', '%3A')
    encoded_end_date = end_date_str.replace(':', '%3A')

    weather_values_url = f'https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{encoded_init_date}/fechafin/{encoded_end_date}/estacion/{ema_code_value}'

    # Obtengo los datos de Getafe en las fechas solicitadas
    res = requests.get(weather_values_url, headers=headers).json()
    data_getafe_url = res['datos']
    data_getafe = requests.get(data_getafe_url).json()

    avg_temp = data_getafe[0]['tmed']

    print('|------------------------------------------------------------------------------------------------------|')
    print('|   ¿Cuantas requests os hacen falta hacer?                                                            |')
    print('| R--> He tenido que hacer 4 request para obtener la respuesta                                         |')
    print('|------------------------------------------------------------------------------------------------------|')
    print('|   ¿Cómo vais a meter Getafe?                                                                         |')
    print('| R--> En las dos primeras request se obtienen los datos de Getafe                                     |')
    print('|------------------------------------------------------------------------------------------------------|')
    print('|   ¿cuál es la request final?                                                                         |')
    print('| R--> "data_getafe" tiene la request final con la url de los datos meteorológicos obtenidos           |')
    print('|------------------------------------------------------------------------------------------------------|')
    print('|   Respuesta final es:                                                                                |')
    print(f'| La temperatura media en Getafe entre {init_date_str} y {end_date_str} ha sido: {avg_temp} ºC |')
    print('|------------------------------------------------------------------------------------------------------|')
    return avg_temp