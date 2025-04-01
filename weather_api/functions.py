import pandas as pd
import requests
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")

    def encode_location(texto):
        return urllib.parse.quote(texto)
    
    encoded_city = encode_location(city)

    url = f'http://api.weatherapi.com/v1/current.json?q={encoded_city}&lang=es&key={api_key}'

    try:
        # Obtengo el código EMA de la Estacion de GETAFE
        response = requests.get(url).json()
        location = response['location']
        current = response['current']
        condition = response['current']['condition']

        # Location DF
        location_df = pd.DataFrame([location]).fillna('no_data')

        # Current DF
        current_df = pd.DataFrame([current]).iloc[:, :5].fillna(0)

        # Condition DF
        condition_df = pd.DataFrame([condition]).iloc[:, :3].fillna(0)

        # Wind DF
        wind_df = pd.DataFrame([current]).iloc[:, [6,7,8,9,27,28]].fillna(0)

        # Presure DF
        presure_df = pd.DataFrame([current]).iloc[:, 10:12].fillna(0)

        # Rain DF
        rain_df = pd.DataFrame([current]).iloc[:, 12:14].fillna(0)

        # Humidity and Dewpoint DF
        humidity_and_dewpoint_df = pd.DataFrame([current]).iloc[:, [14,22,23]].fillna(0)

        # Temperature DF
        temperature_df = pd.DataFrame([current]).iloc[:, 16:22]

        # Visibility DF
        visibility_df = pd.DataFrame([current]).iloc[:, 24:26]

        # UV Index DF
        uv_index_df = pd.DataFrame([current]).iloc[:, 26:27]


        condition_ico = condition_df['icon'].values[0]

        current_df['condition'] = condition_ico

        if condition_ico.startswith('//'):
            condition_ico = 'https:' + condition_ico
        elif condition_ico.startswith('/'):
            condition_ico = 'https://cdn.weatherapi.com' + condition_ico

        
        all_info = (
            location_df,
            current_df,
            condition_df,
            wind_df,
            presure_df,
            rain_df,
            humidity_and_dewpoint_df,
            temperature_df,
            visibility_df,
            uv_index_df
        )


        # final_df = pd.concat([
        #     location_df,
        #     current_df
        # ], axis=1)

        #almacenar los dataframe en un txt
        # with open("wheater.txt", "w", encoding='utf-8') as file:
        #      file.write(final_df.to_string(index=False))
            
        # file.close()

        return all_info
    except Exception as e:
        print(f'Error inesperado {e}')