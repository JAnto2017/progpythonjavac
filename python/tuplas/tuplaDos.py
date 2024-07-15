# Tuplas en Python

# Tupla de nombres

nombres = ('Juan', 'Pedro', 'Maria')

# Tupla de números

numeros = (10, 20, 30, 40, 50)

# recorrer una tupla de nombres

for nombre in nombres:
    print(nombre, end=' ')

# recorrer una tupla de números

for numero in numeros:
    print(numero, end='')

# acceder a un elemento de una tupla

print(f'Elemento 0 de la tupla: {nombres[0]}')  # Juan

print(f'Elemento 2 de la tupla: {numeros[2]}')  # 30

# acceder a un elemento de una tupla de izquierda a derecha

print(f'Último elemento de la tupla: {nombres[-1]}')  # Maria

print(f'Penúltimo elemento de la tupla: {numeros[-2]}')  # 40

# buscar un número dentro de la tupla

print(f'10 está en la tupla: {"10" in nombres}')  # True

print(f'60 está en la tupla: {"60" in numeros}')  # False

