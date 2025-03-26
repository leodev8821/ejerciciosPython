from examen_python import exam_p2
from ejercicio_freecurrencyAPI import currency_converter

#1. ejercicio1:
# Saca la distancia a los restaurantes y la calificación de los usuarios en el dataframe, dad el nombre del más cercano y 
# del mejor valorado de los de alrededor
# Cread la tabla en un esquema en vuestra base de datos
def solucion1():
    #TODO
    print('Not implemented yet...')
    return None

#2. Ejercicio 2:
#suponiendo que el precio está en dólares, ¿cuantas libras ha costado si lo hubieramos hecho hoy?
def solucion2():
    bougth_amount_USD = exam_p2()
    total_in_BP = currency_converter(base_amount=bougth_amount_USD, base_currency='USD', currencies=['GBP'])
    print(f'El valor de la compra en ha sido {bougth_amount_USD} USD que en libras es {total_in_BP} GBP')
    return total_in_BP