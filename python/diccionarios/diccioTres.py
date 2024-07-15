# Diccionarios en Python

# Obtener una lista de las llaves de nuestro diccionario

diccionario = {'a': 1, 'b': 2, 'c': 3}
llaves = list(diccionario.keys())
print(llaves)   # ['a', 'b', 'c']

# Obtener una lista de los valores de nuestro diccionario

print(f'Lista de los valores de nuestro diccionario: {diccionario.values()}')

# Obtener una lista de los elementos del diccionario (items)

print(f'Lista de los elementos del diccionario {diccionario.items()}')
