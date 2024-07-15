
# Diccionario en python de varios elementos de distintos tipos

# Diccionario en python de varios elementos de distintos tipos

# Definimos el diccionario

diccionario = {
    'string': 'Este es un string',
    'entero': 123,
    'flotante': 123.456,
    'boleano': True,
    'lista': ['elemento1', 'elemento2', 'elemento3'],
    'diccionario': {'subelemento1': 'valor1', 'subelemento2': 'valor2'},
    'funcion': lambda x: x * 2
}

# Mostramos cada elemento del diccionario

for clave, valor in diccionario.items():
    print(f'Clave: {clave}, Valor: {valor}')

# Acceder a un elemento de los diccionarios

print(f"Elemento string: {diccionario['string']}")
print(f"Elemento entero: {diccionario['entero']}")
print(diccionario['flotante'])
print(diccionario['boleano'])
print(diccionario['lista'][1])

# Método get en los diccionarios

print(diccionario.get('flotante', 'Valor por defecto'))

# determinar la longitud de un diccionario

print(f'El número de elementos es {len(diccionario)}')

# Agregar un nuevo elemento al diccionario

diccionario['nuevo_elemento'] = 'valor_nuevo'
print(diccionario)