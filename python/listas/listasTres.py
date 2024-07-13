# Listas en Python

# Lista de números

numeros = [11, 22, 33, 44, 55]

# Recuperar una sublista de números. lista[índice_inicio:índice_final - 1]

numeros_pares = numeros[::2]

print (f"La lista = {numeros} tiene los en los índices pares = {numeros_pares}")

# Recuperar una sublista 

    # desde el índice 2 hasta el final

numeros_impares = numeros[2:]

print (f"La lista = {numeros} tiene los en los índices impares = {numeros_impares}")

# Recuperar una sublista indicando el índice final

numeros_impares_final = numeros[:4]

print (f"La lista = {numeros} tiene los en los índices impares (final) = {numeros_impares_final}")

# Realizar una copia de la lista

copia_numeros = numeros.copy()

print (f"La lista copia = {copia_numeros}")

# Añadir un elemento al final de la lista

copia_numeros.append(66)

print (f"La lista copia después de añadir un elemento = {copia_numeros}")

