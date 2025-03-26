from primer_bloque import ejercicio1, ejercicio2, ejercicio3, ejercicio4
from segundo_bloque import ejercicioB2_1, ejercicioB2_2
from ejercicio_pandas import open_connection, make_dataframe, best_cripto
from ejercicio_freecurrencyAPI import buy_sell_INR_with_TRY, any_request_freecurrency_api, currency_converter
from ejercicio_multipleAPI import multiAPI
from examen_python import exam_p1, exam_p2
from ejercicio_API_AEMET import solucion

# Parámetros de las funciones de los ejercicios
strs = ["flower", "flow", "flight", "flowers"]
numlist = [1,2,3,4]
menu = [("pizza", 8.5), ("hamburguesa", 7.0), ("ensalada", 5.5), ("pasta", 6.0)]
pedido_cliente = ["pizza", "pasta", "sopa", "pasta"]
coins = ['dogecoin','ethereum','tether', 'bitcoin']

def main():
    while True:
        print("\n*** MENÚ DE EJERCICIOS ***")
        print("1. Primer Bloque")
        print("2. Segundo Bloque")
        print("3. Ejercicio Pandas")
        print("4. Ejercicio FreeCurrencyAPI")
        print("5. Ejercicio MultipleAPI")
        print("6. Examen Python")
        print("7. Ejercicio API AEMET")
        print("8. Terminar la ejecución")
        
        seleccion = input("Selecciona una opción: ").upper()
        
        match seleccion:
            case "1":
                print("\n*** 1. PRIMER BLOQUE ***")
                print("1. Ejecutar ejercicio 1")
                print("2. Ejecutar ejercicio 2")
                print("3. Ejecutar ejercicio 3")
                print("4. Ejecutar ejercicio 4")
                print("5. Volver")
                
                subseleccion = input("Selecciona una opción: ").upper()
                match subseleccion:
                    case "1":
                        exam_p1(strs)
                    case "2":
                        exam_p2(strs)
                    case "3":
                        ejercicio3(strs)
                    case "4":
                        ejercicio4(strs)
                    case "5":
                        continue
                    case _:
                        print("Opción no válida")
                        
            case "2":
                print("\n*** 2. SEGUNDO BLOQUE ***")
                print("1. Ejecutar ejercicio 1")
                print("2. Ejecutar ejercicio 2")
                print("3. Volver")
                
                subseleccion = input("Selecciona una opción: ").upper()
                match subseleccion:
                    case "1":
                        ejercicioB2_1(numlist)
                    case "2":
                        ejercicioB2_2(menu, pedido_cliente)
                    case "3":
                        continue
                    case _:
                        print("Opción no válida")
                        
            case "3":
                print("\n*** 3. EJERCICIO PANDAS ***")
                print("1. Ejecutar ejercicio 1")
                print("2. Ejecutar ejercicio 2")
                print("3. Ejecutar ejercicio 3")
                print("4. Volver")
                
                subseleccion = input("Selecciona una opción: ").upper()
                match subseleccion:
                    case "1":
                        open_connection()
                    case "2":
                        make_dataframe()
                    case "3":
                        best_cripto(coins)
                    case "4":
                        continue
                    case _:
                        print("Opción no válida")
                        
            case "4":
                print("\n*** 4. EJERCICIO FreeCurrencyAPI ***")
                print("1. Ejecutar ejercicio 1")
                print("2. Ejecutar ejercicio 2")
                print("3. Ejecutar ejercicio 3")
                print("4. Volver")

                subseleccion = input("Selecciona una opción: ").upper()
                match subseleccion:
                    case "1":
                        buy_sell_INR_with_TRY()
                    case "2":
                        print("Request para obtener el valor del EUR en USD y CAD en 02-enero-2024")
                        any_request_freecurrency_api(type='historical', date='2024-01-02', base_currency='EUR', currencies=['EUR','USD','CAD'])
                    case "3":
                        print("Convertir 10 EUR en Lira Turca")
                        currency_converter(base_amount=10,base_currency="EUR", currencies=['TRY'])
                    case "4":
                        continue
                    case _:
                        print("Opción no válida")
            
            case "5":
                print("\n*** 5. EJERCICIO MultipleAPI ***")
                print("1. Ejecutar el ejercicio")
                print("2. Volver")

                subseleccion = input("Selecciona una opción: ").upper()
                match subseleccion:
                    case "1":
                        multiAPI()
                    case "2":
                        continue
                    case _:
                        print("Opción no válida")

            case "6":
                print("\n*** 6. EXÁMEN PYTHON ***")
                print("1. Ejecutar el ejercicio 1")
                print("2. Ejecutar el ejercicio 2")
                print("3. Volver")

                subseleccion = input("Selecciona una opción: ").upper()
                match subseleccion:
                    case "1":
                        exam_p1()
                    case "2":
                        exam_p2()
                    case "3":
                        continue
                    case _:
                        print("Opción no válida")
            case "7":
                print("\n*** 7. Ejercicio API AEMET ***")
                print("1. Ejecutar la solución")
                print("2. Volver")

                subseleccion = input("Selecciona una opción: ").upper()
                match subseleccion:
                    case "1":
                        solucion()
                    case "2":
                        continue
                    case _:
                        print("Opción no válida")
            case "8":
                break
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    main()