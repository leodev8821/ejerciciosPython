'''Enunciado del ejercicio:
Imagina que compras el artículo llamado "Rain Jacket Women Windbreaker Striped Climbing Raincoats" de la tienda FakeStoreAPI, 
cuyo precio está en dólares estadounidenses (USD). El día 26 de enero de 2020, realizas la compra pagando en rublos (RUB), 
es decir, conviertes la cantidad necesaria de rublos para cubrir el precio en dólares de la chaqueta.
El 3 de marzo de 2022, vendes la chaqueta por el mismo precio en dólares (USD) que pagaste originalmente. Sin embargo, 
esta vez, debido a la inflación del rublo, recibes el equivalente en rublos (RUB) al tipo de cambio de esa fecha 
(que será considerablemente más alto debido a la devaluación del rublo en ese período).
Luego, el 1 de septiembre de 2024, usas los rublos obtenidos de la venta para comprar florines húngaros (HUF).
Finalmente, el día de ayer, usas esos florines húngaros para comprar Ethereum (ETH), utilizando el precio de Ethereum de ese día.
 Preguntas:
1. ¿Cuántos rublos (RUB) pagaste por el abrigo el 26 de enero de 2020?
2. ¿Por cuántos rublos (RUB) vendiste el abrigo el 3 de marzo de 2022, considerando la inflación del rublo?
3. ¿Cuántos florines húngaros (HUF) obtuviste el 1 de septiembre de 2024 al convertir los rublos de la venta?
4. ¿Qué cantidad de Ethereum (ETH) obtuviste ayer al convertir los florines húngaros?
 Instrucciones:
- El precio del artículo en USD debe obtenerse desde FakeStoreAPI.
- Las conversiones de moneda deben realizarse usando APIs de tasas de cambio (por ejemplo, FreeCurrencyAPI para obtener las 
tasas históricas de conversión).
- El precio de Ethereum (ETH) debe obtenerse usando la API de CoinGecko, para el día de ayer.
Este enunciado ahora refleja claramente que compras el abrigo en rublos, lo vendes en rublos al valor equivalente en dólares 
en 2022, y luego realizas las conversiones adicionales.'''
from datetime import datetime, timezone, timedelta
import requests
from ejercicio_freecurrencyAPI import any_request_freecurrency_api

def multiAPI():
    # Obtener la fecha de ayer
    yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime('%d-%m-%Y')
    coin_geko_url = f'https://api.coingecko.com/api/v3/coins/ethereum/history?date={yesterday}'
    fake_store_url = f'https://fakestoreapi.com/products/17'

    # Obtiene el precio del producto
    response = requests.get(fake_store_url)
    response.raise_for_status()
    data = response.json()
    price_USD = data['price']

    #'día 26 de enero de 2020, realizas la compra pagando en rublos (RUB)'
    priceRUB2USD = any_request_freecurrency_api(type='historical', date='2020-01-26', base_currency='RUB', currencies=['USD'])
    valueRUB = round(priceRUB2USD['data']['2020-01-26']['USD'],2)
    price_RUB = round(price_USD / valueRUB)
    print(f'Para pagar {price_USD} USD ha usado {price_RUB} RUB')

    #El 3 de marzo de 2022
    priceUSD2RUB = any_request_freecurrency_api(type='historical', date='2022-03-03', base_currency='USD', currencies=['RUB'])
    valueUSD = round(priceUSD2RUB['data']['2022-03-03']['RUB'],2)
    sell_price_RUB = round(price_USD * valueUSD)
    print(f'AL vender en {price_USD} USD ha obtenido {sell_price_RUB} RUB')

    #1 de septiembre de 2024 HUF
    priceRUB2HUF = any_request_freecurrency_api(type='historical', date='2024-09-01', base_currency='RUB', currencies=['HUF'])
    valueUHF = round(priceRUB2HUF['data']['2024-09-01']['HUF'],2)
    price_HUF = round(sell_price_RUB * valueUHF)
    print(f'AL vender {sell_price_RUB} RUB ha obtenido {price_HUF} HUF')

    #el día de ayer, usas esos florines húngaros para comprar Ethereum (ETH), utilizando el precio de Ethereum de ese día.
    response= requests.get(coin_geko_url).json()
    ethPrice = response['market_data']['current_price']['huf']
    total_coin = round((ethPrice / price_HUF),2)
    print(f'Con {price_HUF} HUF ha obtenido {total_coin} ETH')
    
    return (price_USD,price_RUB,sell_price_RUB,price_HUF,total_coin)