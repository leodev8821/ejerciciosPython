import requests
import os
from dotenv import load_dotenv

load_dotenv()

def solucion():
    api_key = os.getenv("AEMET_API_KEY")
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

    querystring = {"api_key":api_key}

    headers = {
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
