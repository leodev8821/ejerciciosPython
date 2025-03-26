
import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

#Ejercicio 1: Tenéis que, usando las APIs de places y geolocation obtener los restaurantes que hay en un radio de un km de 
# aquí (Avenida Manoteras 26, 28050 Madrid) la respuesta debe estar en un dataframe con al menos el nombre del restaurante y 
# su dirección
def exam_p1():
    #TODO
    print('Not implemented yet...')
    return None

#Ejercicio 2: Conectaros a la base de datos de northwind y sacad los productos de la tabla productos queremos hacer una compra 
# de productos (northwind.Products). Esa compra está en un fichero excel, tenéis que dar el precio total de la compra en formato float. 
# Restricciones:
#No puede haber api keys directamente en el código, las teneis que leer de algún fichero
#Cada ejercicio debe ir en una función podéis usar funciones auxiliares sin límite
#Fijaros en el formato de la respuesta, el resultado tiene que estar en lo que se os pide
def dbConnection():
    try:
        MY_HOST = os.getenv("HOST")
        MY_DATABASE = os.getenv("DATABASE")
        MY_USER = os.getenv("USER")
        MY_PASSWORD = os.getenv("PASSWORD")
        MY_PORT = os.getenv("PORT")
        
        conn = psycopg2.connect(
            dbname=MY_DATABASE,
            user=MY_USER,
            password=MY_PASSWORD,
            host=MY_HOST,
            port=MY_PORT
        )
        print("Conexión exitosa")
        cur = conn.cursor()
        return conn, cur

    except psycopg2.Error as e:
        print(f"Error de conexión: {str(e)}")
        return None

def exam_p2():
    conn, cur = dbConnection()

    try:
        sql = 'select product_name, unit_price from products;'
        cur.execute(sql)
        rows = cur.fetchall()

        df = pd.DataFrame(rows, columns=['product_name', 'unit_price'])
        df['quantity'] = ""

        # Si el Excel no existe, lo crea
        if not os.path.exists('products.xlsx'):
            with pd.ExcelWriter('products.xlsx',mode='w',engine='openpyxl') as writer:
                df.to_excel(
                    writer,
                    sheet_name='products',
                    index=False
                )      
        
        # Leo y filtro solo los productos que tienen algún valor en 'quantity'
        rdf = pd.read_excel('products.xlsx')
        rdf_filtrado = rdf.dropna(subset=['quantity'])

        # Obtengo el precio unitario y la cantidad para operar sobre ellos
        unit_price = rdf_filtrado['unit_price']
        quantity = rdf_filtrado['quantity']

        # Sumo el total
        total_amount = (unit_price * quantity).sum()

        print(f'El precio total de la compra ha sido de {total_amount} USD')
        return total_amount
    except psycopg2.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        if conn is not None:
            conn.close()