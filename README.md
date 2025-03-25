# Ejecución
Ejecutar el main.py y alli salen los menus
```python .\main.py```
# Manuales y ejercicios de Python

https://python-docs-es.readthedocs.io/es/3.12/tutorial/index.html
https://j2logo.com/python/tutorial/

# Primer bloque de ejercicios --> ✅
Ejercicios sobre Cadenas
Dada una lista de palabras, como la siguiente:
strs = ["flower", "flow", "flight", "flowers"]
Deberás realizar las siguientes actividades relacionadas con cadenas de texto, creando una **función** para cada ejercicio.
---
1. Ejercicio 1: Longitud de la Cadena Más Larga
Crea una función que devuelva la longitud de la palabra más larga de la lista strs. Por ejemplo, en el caso de la lista dada, la función debería devolver `7`, ya que la palabra más larga es "flowers", que contiene 7 letras.
---
2. Ejercicio 2: Longitud de la Cadena Más Larga y Más Corta
Crea una función que devuelva tanto la longitud de la palabra más larga como la longitud de la palabra más corta de la lista `strs`. La función debe devolver ambas longitudes en una misma estructura de datos (por ejemplo, una tupla o un diccionario).
Para la lista de ejemplo, la función debería devolver 7 como longitud máxima (por "flowers") y `4` como longitud mínima (por "flow").
---
3. Ejercicio 3: Prefijo Común Más Largo
Escribe una función que encuentre el prefijo común más largo entre todas las palabras de la lista `strs`. El prefijo común es la parte del principio de las palabras que todas comparten. 
Por ejemplo:
- Para la lista `["flower", "flow", "flight"]`, el prefijo común más largo sería `"fl"`.
- Para la lista `["madera", "madrid", "madrugar"]`, el prefijo común sería `"mad"`.
- Si no hay ningún prefijo común, como en `["sal", "cal", "vals"]`, la función debería devolver una cadena vacía "".
Nota: Esto se puede hacer con un solo bucle, pero de momento hacedlo como podáis
---
4. Ejercicio 4: Escritura de Resultados en Archivo
Usando las funciones anteriores, crea una función que escriba cada resultado en un archivo llamado `salida.txt`. El archivo debe generarse en la misma carpeta en la que estáis trabajando.
Cada resultado debe estar en una nueva línea dentro del archivo. aquí tenéis información sobre como leer y escribir archivos en Python: https://www.freecodecamp.org/espanol/news/lectura-y-escritura-de-archivos-en-python-como-crear-leer-y-escribir-archivos/.
---
Restricciones de los Ejercicios
- La lista debe contener, como mínimo, dos palabras.
- Todas las palabras deben estar compuestas únicamente por letras minúsculas.
- Cada palabra debe tener al menos una letra.

# Segundo bloque de ejercicios --> ✅
Ejercicios de estructuras de datos más avanzadas:

1. Ejercicio1: 
Dada una lista de números
por ejemplo numlist = [1,2,3,4]
teneis que devolver true si hay duplicados y False si no los hay 
numlist = [1,2,3,4] devolvería False pero numlist = [1,1,2,3,4] devolvería True

2. Ejercicio 2: 
Crear una función que tiene 2 argumentos menú y pedido_cliente
menu = [("pizza", 8.5), ("hamburguesa", 7.0), ("ensalada", 5.5), ("pasta", 6.0)]
pedido_cliente = ["pizza", "pasta", "sopa"]
menú es una lista de tuplas donde el primer elemento es lo que pides y el segundo es un float que es el precio
el pedido es una lista de lo que pides
Teneis que devolver un ticket de compra como este donde le dais los platos que ha pedido y están en el menú y di no lo está no los añades al ticket pero no das error
luego das el precio total, en algo como esto
{
  "pizza": 8.5,
   "pasta": 6.0
y en la misma función también das el precio que serían 14.5
el menú no puede tener platos repetidos.

# Video Pandas
    https://www.youtube.com/watch?v=8ASjvOIyyl8

# Guía Instalación VENV
    - Abrís la terminal de vdcode 
    - Instalar venv en python (si es que no lo habeis instalado antes)
        python -m pip install --upgrade pip
        pip install virtualenv
    - Compruebas que estás dentro
        virtualenv --version
    - Creas tu entorno virtual llamado venv
        virtualenv  ./venv 
    - Asi lo activas y estas dentro
        .\venv\Scripts\Activate.ps1
    - Si no os deja por tema de permisos probad esto y volved a intentar activarlo, probablemente funcione
        Get-ExecutionPolicy -List
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    - instalais algunos paquetes
        pip install psycopg2
        pip install pandas
    - ahora volcamos en un requirements.txt las versiones
        pip freeze > requirements.txt

 
# Ejercicios PANDAS --> ✅
    https://docs.coingecko.com/v3.0.1/reference/introduction
1. Ejercicio 1:
hacer una función llamada open_connection que te conecte a la base de datos usando psycopg2, los parámetros host,database,user,password y port
La función debe tener por argumento un fichero json con las credenciales necesarias para conectarse a la bbdd

2. Ejercicio 2:
hagan una función que
    1. se conecten a la base de datos al esquema de northwind (usando la función de antes)
    2. devuelvan el id y precio total de la orden de id 10248 (order_details) en un dataframe

3. Ejercicio 3:
La función del ejercicio anterior os ha devuelto el resultado en dólares (es decir el precio vamos a decir que son dólares), 
os tenéis que conectar al api de coingecko y hacer una función que devuelva el nombre de la criptodivisa que os salga la compra por más criptomenedas y teneis que devolver una tupla con el nombre de la criptodivisa y el precio medido en esa criptodivisa

# Ejercicios FreecurrencyAPI --> ✅
    https://app.freecurrencyapi.com
Usando freecurency api vamos a comprar el día 1 de enero de 2023 rupias indias con 200 liras turcas, el 4 de marzo de 2024 vamos a venderlas y comprar otra vez las liras turcas
1. Una función que haga cualquier request contra free currency api
2. Una función que haga la conversión entre monedas

 
# Ejercicios múltiples APIS --> ✅
https://fakestoreapi.com/

Enunciado del ejercicio:
Imagina que compras el artículo llamado "Rain Jacket Women Windbreaker Striped Climbing Raincoats" de la tienda FakeStoreAPI, cuyo precio está en dólares estadounidenses (USD). El día 26 de enero de 2020, realizas la compra pagando en rublos (RUB), es decir, conviertes la cantidad necesaria de rublos para cubrir el precio en dólares de la chaqueta.
El 3 de marzo de 2022, vendes la chaqueta por el mismo precio en dólares (USD) que pagaste originalmente. Sin embargo, esta vez, debido a la inflación del rublo, recibes el equivalente en rublos (RUB) al tipo de cambio de esa fecha (que será considerablemente más alto debido a la devaluación del rublo en ese período).
Luego, el 1 de septiembre de 2024, usas los rublos obtenidos de la venta para comprar florines húngaros (HUF).
Finalmente, el día de ayer, usas esos florines húngaros para comprar Ethereum (ETH), utilizando el precio de Ethereum de ese día.
 Preguntas:
1. ¿Cuántos rublos (RUB) pagaste por el abrigo el 26 de enero de 2020?
2. ¿Por cuántos rublos (RUB) vendiste el abrigo el 3 de marzo de 2022, considerando la inflación del rublo?
3. ¿Cuántos florines húngaros (HUF) obtuviste el 1 de septiembre de 2024 al convertir los rublos de la venta?
4. ¿Qué cantidad de Ethereum (ETH) obtuviste ayer al convertir los florines húngaros?
 Instrucciones:
- El precio del artículo en USD debe obtenerse desde FakeStoreAPI.
- Las conversiones de moneda deben realizarse usando APIs de tasas de cambio (por ejemplo, FreeCurrencyAPI para obtener las tasas históricas de conversión).
- El precio de Ethereum (ETH) debe obtenerse usando la API de CoinGecko, para el día de ayer.
Este enunciado ahora refleja claramente que compras el abrigo en rublos, lo vendes en rublos al valor equivalente en dólares en 2022, y luego realizas las conversiones adicionales.
 
# Ejercicio API AEMET
Usando la API de AEMET, vais a tener que buscar la temperatura media que hizo en getafe entre el 22 y 23 de agosto de este año a las 10:30 (2024-08-22T08:30:30UTC)
(2024-08-23T08:30:30UTC)
Pasos
Conseguid la api key (la api key no puede ir directamente en el código)
Mirad como se hacen las requests
¿Cuantas requests os hacen falta hacer? ¿Cómo vais a meter getafe?
¿cuál es la request final?

# Examen python
1. Ejercicio 1: Tenéis que, usando las APIs de places y geolocation obtener los restaurantes que hay en un radio de un km de aquí (Avenida Manoteras 26, 28050 Madrid) la respuesta debe estar en un dataframe con al menos el nombre del restaurante y su dirección
2. Ejercicio 2: Conectaros a la base de datos de northwind y sacad los productos de la tabla productos queremos hacer una compra de productos (northwind.Products). Esa compra está en un fichero excel, tenéis que dar el precio total de la compra en formato float.
Restricciones: 
1.	No puede haber api keys directamente en el código, las teneis que leer de algún fichero
2. Cada ejercicio debe ir en una función podéis usar funciones auxiliares sin límite
3. Fijaros en el formato de la respuesta, el resultado tiene que estar en lo que se os pide

# Puntos extra:
1. ejercicio1:
Saca la distancia a los restaurantes y la calificación de los usuarios en el dataframe, dad el nombre del más cercano y del mejor valorado de los de alrededor
Cread la tabla en un esquema en vuestra base de datos

2. Ejercicio 2:
suponiendo que el precio está en dólares, ¿cuantas libras ha costado si lo hubieramos hecho hoy?