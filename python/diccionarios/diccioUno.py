# Diccionarios en Python

# Diccionario vacío

diccionario = {}

# Diccionario con pares clave-valor

diccionario = {
    'clave1': 'valor1',
    'clave2': 'valor2',
    'clave3': 'valor3'
}

# Añadir un par clave-valor

diccionario['clave4'] = 'valor4'

# Modificar un valor

diccionario['clave1'] = 'nuevo_valor1'

# Eliminar un par clave-valor

del diccionario['clave2']

# Diccionario con pares clave-valor de distintos tipos de datos

diccionario = {
    'clave1': 123,
    'clave2': True,
    'clave3': ['valor1', 'valor2', 'valor3'],
    'clave4': {'subclave1': 'valor4', 'subclave2': 'valor5'}
}

# Acceder a un valor por clave

valor_clave1 = diccionario['clave1']

valor_clave4_subclave1 = diccionario['clave4']['subclave1']

# Comprobar si una clave existe

if 'clave5' in diccionario:
    print('La clave existe')
else:
    print('La clave no existe')
    