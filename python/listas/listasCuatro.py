# Métodos en las Listas

# Lista de números

numeros = [1, 2, 3, 4, 5]

# Longitud de una lista

longitud_numeros = len(numeros)
print(longitud_numeros)  # Output: 5

# Agregar un elemento al final de la lista

numeros.append(6)
print(numeros)  # Output: [1, 2, 3, 4, 5, 6]

# Insertar nuevos elementos en la posicion de la lista

numeros.insert(2, 7)
print(numeros)  # Output: [1, 2, 7, 3, 4, 5, 6]

# Eliminar un elemento de la lista

numeros.remove(3)   # se indica el elemento de la lista
print(numeros)  # Output: [1, 2, 7, 4, 5, 6]

# Concatenar listas

otros_numeros = [8, 9, 10]
numeros_concatenados = numeros + otros_numeros
print(f'Lista a: {numeros} lista b: {otros_numeros} lista concatenada {numeros_concatenados}')  # Output: [1, 2, 7, 4, 5, 6, 8, 9, 10]

# Eliminar un elemento por índice

print(f'Lista antes de eliminar el índice 3: {numeros_concatenados}')
del numeros_concatenados[3]
print(f'Lista después de eliminar el índice 3: {numeros_concatenados}')  # Output: [1, 2, 7, 5, 6, 8, 9, 10]