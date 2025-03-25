# 1. Ejercicio 1: Longitud de la Cadena Más Larga
def ejercicio1(words):
    longest = max(words, key=len)
    size = len(longest)
    print(f"La cadena mas larga tiene un tamaño de {size}")
    return size

#2. Ejercicio 2: Longitud de la Cadena Más Larga y Más Corta
def ejercicio2(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    print(f"La cadena mas larga tiene un tamaño de {len(longest)} y la más corta de {len(shortest)}")
    return (longest, shortest)

# 3. Ejercicio 3: Prefijo Común Más Largo
def ejercicio3(words):
    prefix = ""
    for i in range(len(words[0])):
        current_char = words[0][i]

        for word in words:
            if i >= len(word) or word[i] != current_char:
                return prefix
        
        prefix += current_char

    print(f"El prefijo común más largo es {prefix}")
    return prefix

# 4. Ejercicio 4: Escritura de Resultados en Archivo
def ejercicio4(words):
    result1 = ejercicio1(words)
    result2 = f"La cadena mas larga tiene un tamaño de {ejercicio2(words)[0]} y la más corta de {ejercicio2(words)[1]}"
    result3 = ejercicio3(words)

    file = open("salida.txt", "w")

    file.writelines(f'''Ejercicio 1: {result1}\nEjercicio 2: {result2}\nEjercicio 3: {result3}''')

    file.close()