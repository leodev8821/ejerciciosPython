import os
import psycopg2
from psycopg2 import Error
import json
import pandas as pd
import requests

# 1. Ejercicio 1:
# hacer una función llamada open_connection que te conecte a la base de datos usando psycopg2, 
# los parámetros host,database,user,password y port
# La función debe tener por argumento un fichero json con las credenciales necesarias para conectarse a la bbdd
def open_connection(credentials='credentials.json'):
    try:
        script_dir = os.path.dirname(__file__)
        credentials_path = os.path.join(script_dir, credentials)
        
        with open(credentials_path, 'r') as archive:
            credentials = json.load(archive)
        conn = psycopg2.connect(
            dbname=credentials['database'],
            user=credentials['user'],
            password=credentials['password'],
            host=credentials['host'],
            port=credentials['port']
        )
        print("Conexión exitosa")
        cur = conn.cursor()

        return conn, cur

    except Error as e:
        print(f"Error de conexión: {str(e)}")
        return None
    
# 2. Ejercicio 2:
# hagan una función que
#     1. se conecten a la base de datos al esquema de northwind (usando la función de antes)
#     2. devuelvan el id y precio total de la orden de id 10248 (order_details) en un dataframe
def make_dataframe():
    conn, cursor = open_connection()

    try:
        sql = '''select order_id, round(sum(unit_price*quantity)) from order_details where order_id = 10248 group by order_id'''
        cursor.execute(sql)
        rows = cursor.fetchall()
        df = pd.DataFrame(columns=['Order_ID', 'Total_Price'])
        for row in rows:
            df.loc[len(df)] = [row[0], row[1]]
        conn.close()
        return df
    except psycopg2.Error as e:
        print(f"Error al ejecutar la consulta: {e}")

# 3. Ejercicio 3:
# La función del ejercicio anterior os ha devuelto el resultado en dólares (es decir el precio vamos a decir que son dólares), 
# os tenéis que conectar al api de coingecko y hacer una función que devuelva el nombre de la criptodivisa que os salga 
# la compra por más criptomonedas y teneis que devolver una tupla con el nombre de la criptodivisa y el precio medido en esa 
# criptodivisa
def best_cripto(coins):
    try:
        # recibo el datagrame y capturo el valor del precio total
        df = make_dataframe()
        order_price = df.loc[0, 'Total_Price']

        print(df)

        url = f"https://api.coingecko.com/api/v3/simple/price"
        
        # Uno el array de coins que recibe como parámetro
        ids = ",".join(coins)

        # se construye el objeto de los parámetros por GET
        params = {
                'ids': ids,
                'vs_currencies': 'usd',
                'include_market_cap' : 'true'
            }

        headers = {"accept": "application/json"}

        # se realiza el fetch a al url con los parámetros
        response = requests.get(url, params,headers=headers)

        # se convierte la respuesta en JSON para tratar los datos
        data = response.json()

        # obtengo el número de monedas de la primera coin que se recibe
        coins_number = order_price / data[coins[0]]['usd']
        best_coin = coins[0]

        # se recorre el array de coins recibidas
        for coin in coins:
            # se hace el cálculo de la cantidad de monedas
            coins_num = order_price / data[coin]['usd']
                
            # se verifica que el número de monedas sea mayor al que se tiene
            if coins_num > coins_number:
                coins_number = coins_num
                best_coin = coin

        return (best_coin,coins_number)

    except requests.exceptions.RequestException as e:
        print(f"Error en la petición HTTP: {str(e)}")
        return None
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return None