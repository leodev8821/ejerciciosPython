import freecurrencyapi
import requests
import os
from dotenv import load_dotenv

load_dotenv()

"""     https://app.freecurrencyapi.com
Usando freecurency api vamos a comprar 
--> el día 1 de enero de 2023 rupias indias con 200 liras turcas
--> el 4 de marzo de 2024 vamos a venderlas
--> el mismo día comprar otra vez las liras turcas
 """
def buy_sell_INR_with_TRY():
    try:
        api_key = os.getenv("FREECURRENCY_API_KEY")
        client = freecurrencyapi.Client(f"{api_key}")

        first_move = client.historical(date='2023-01-01', base_currency='TRY', currencies=['INR'])
        second_move = client.historical(date='2024-03-04', base_currency='TRY', currencies=['INR'])

        buy_rupees = round(first_move['data']['2023-01-01']['INR'] * 200,2)
        sell_rupees = round(buy_rupees / second_move['data']['2024-03-04']['INR'],2)
        new_buy_rupees = round(second_move['data']['2024-03-04']['INR'] * sell_rupees,2)

        exit_text = f'''
            Movimiento 1 --> 1 de enero de 2023 con 200 TRY se obtienen {buy_rupees} INR.
            Movimiento 2 --> 4 de marzo de 2024 se venden las {buy_rupees} INR y se obtienen {sell_rupees} TRY
            Movimiento 3 --> 4 de marzo de 2024 se compran {new_buy_rupees} INR con {sell_rupees} TRY
            '''
        print(exit_text)
        return exit_text
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return None
    
#buy_sell_INR_with_TRY()

# 1. Una función que haga cualquier request contra free currency api
def any_request_freecurrency_api(type='status', date='2025-01-01', base_currency=None, currencies=[]):
    api_key = os.getenv("FREECURRENCY_API_KEY")
    base_url = f'https://api.freecurrencyapi.com/v1/'
    
    if currencies is None:
        currencies = []
    
    try:
        match type:
            case 'status':
                url = f"{base_url}{type}?apikey={api_key}"
                response = requests.get(url)

            case 'currencies':
                curr = ",".join(currencies)
                params = {
                    'currencies': curr
                }
                url = f"{base_url}{type}?apikey={api_key}"
                response = requests.get(url, params=params)

            case 'latest':
                curr = ",".join(currencies)
                params = {
                    'base_currency': base_currency,
                    'currencies': curr
                }
                base_url += f"{type}?apikey={api_key}"
                response = requests.get(base_url, params)
            
            case 'historical':
                curr = ",".join(currencies)
                params = {
                    'date': date,
                    'base_currency': base_currency,
                    'currencies': curr
                }
                base_url += f"{type}?apikey={api_key}"
                response = requests.get(base_url, params)

            case _:
                print("Opción no válida")
                return None
             
        response.raise_for_status()
        data = response.json()
        #print(data)
        return data

    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return None
    
#any_request_freecurrency_api(type='currencies')
#any_request_freecurrency_api(type='currencies', currencies=['EUR','USD','CAD'])
#any_request_freecurrency_api(type='latest', base_currency='EUR', currencies=['EUR','USD','CAD'])
#any_request_freecurrency_api(type='historical', date='2024-01-02', base_currency='EUR', currencies=['EUR','USD','CAD'])


# 2. Una función que haga la conversión entre monedas
def currency_converter(base_amount=0, base_currency=None, currencies=[]):
    api_key = os.getenv("FREECURRENCY_API_KEY")
    base_url = f'https://api.freecurrencyapi.com/v1/'
    
    if currencies is None:
        raise ValueError("currencies es requerido para la conversión")
    
    if base_currency is None:
        raise ValueError("base_currency es requerido para la conversión")
    
    try:
        currencies.append(base_currency)
        curr = ",".join(currencies)
        params = {
            'base_currency': base_currency,
            'currencies': curr
        }
        base_url += f"latest?apikey={api_key}"
        response = requests.get(base_url, params)
            
             
        response.raise_for_status()
        data = response.json()
        converted_amount = round(base_amount * data['data'][currencies[0]],2)
        exit_text = f'''Al convertir {base_amount} {base_currency} te da {converted_amount} {currencies[0]}'''
        print(exit_text)
        return converted_amount
    
    except requests.exceptions.HTTPError as http_err:
        print(f'Ocurrió un error de HTTP: {http_err}')
        return None
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return None
    
#currency_converter(base_amount=10,base_currency="EUR", currencies=['TRY'])