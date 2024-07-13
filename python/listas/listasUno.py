
# Listas en Python -----------------------------------------------------------
# Conjunto de elementos ------------------------------------------------------

# Lista compuesta de nombres. El primer elemento empieza por 0

nombres = ['Juan', 'Maria', 'Pedro', 'Ana']
print (f'Lista de nombres: {nombres}')

# Lista heterogénea (múltiples tipos de datos)
lista_hetero = [10, True, 'Antonio']
print (f'Lista de lista: {lista_hetero}')

# Iterar o recorrer la lista

for nombre in nombres:
    print(f'Nombre: {nombre}')
    # print(nombre, end=' ') para imprimir en la misma línea

# Lista de números

numeros = [10, 20, 30, 40, 50]

# Acceso a un elemento específico
print(f'accede al índice 0 = {numeros[0]}') 

# modificar los elementos de la lista

numeros[0] = 55
print(f'nueva lista: {numeros}')