
# Crear un diccionario de valores

dict_values = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Actualizar un elemento del diccionario de valores

dict_values['age'] = 31

# Imprimir el diccionario de valores

print(dict_values)

# Eliminar un elemento del diccionario de valores

del dict_values['city']

# Imprimir el diccionario de valores después de la eliminación

print(dict_values)

# Recorrer las llaves de un diccionario de valores

for key in dict_values:
    print(key)

# Añadir un elemento del diccionario de valores

dict_values['country'] = 'USA'

# Imprimir el diccionario de valores después de la adición

print(dict_values)

# Recorrer los elementos de un diccionario como tupla

for key, value in dict_values.items():
    print(f"{key}: {value}")

# Limpiar el diccionario de valores

dict_values.clear()

# Imprimir el diccionario de valores después de la limpieza

print(dict_values)