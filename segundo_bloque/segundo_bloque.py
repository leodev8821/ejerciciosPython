# 1. Ejercicio1: Dada una lista de números teneis que devolver true si hay duplicados y False si no los hay
def ejercicioB2_1(numlist):
    uniqueList = []
    for number in numlist:
        if number in uniqueList:
            print("False")
            return False
        else:
            uniqueList.append(number)
    print("True")
    return True

# 2. Ejercicio 2: Crear una función que tiene 2 argumentos menú y pedido_cliente
# menu = [("pizza", 8.5), ("hamburguesa", 7.0), ("ensalada", 5.5), ("pasta", 6.0)]
# pedido_cliente = ["pizza", "pasta", "sopa"]
# menú es una lista de tuplas donde el primer elemento es lo que pides y el segundo es un float que es el precio
# el pedido es una lista de lo que pides
# Teneis que devolver un ticket de compra como este donde le dais los platos que ha pedido y están en el menú 
# y si no lo está no los añades al ticket pero no das error
# luego das el precio total, en algo como esto
# {
#  "pizza": 8.5,
#   "pasta": 6.0,
#   "total": 14.5
# }
# y en la misma función también das el precio que serían 14.5
# el menú no puede tener platos repetidos.
def ejercicioB2_2(menu, pedido_cliente):
    orden = []
    ticket = {}
    total = 0

    for pedido in pedido_cliente:
        for plato, precio in menu:
            if pedido == plato and pedido not in orden:
                orden.append(pedido)
                total += precio
                ticket[plato] = precio
                ticket["total"] = total
    
    print("\n******* TICKET *********")
    print("** Platos      Precio **\n")
    for elemento in ticket:
        if elemento != 'total':
            print(f'''** {elemento} -----> € {ticket[elemento]:.2f} ** ''')
    print("-" * 25)
    print(f"Total: €{total:.2f}")
    print("*" * 25)

    return ticket