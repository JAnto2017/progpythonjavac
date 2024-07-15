# Lista con Diccionarios

# Crear una lista que contenga un diccionario

# Diccionario 1

diccionario_1 = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 25,
    "direccion": {
        "calle": "Av. Paseo de la Reina",
        "numero": 123,
        "ciudad": "Barcelona"
    }
}

# Diccionario 2

diccionario_2 = {
    "nombre": "Maria",
    "apellido": "García",
    "edad": 30,
    "direccion": {
        "calle": "Calle del Prado",
        "numero": 456,
        "ciudad": "Madrid"
    }
}

# Añadir los diccionarios a la lista

lista_de_diccionarios = [diccionario_1, diccionario_2]

# Imprimir la lista

#print(lista_de_diccionarios)
print(lista_de_diccionarios[0])
print(lista_de_diccionarios[1])

# Acceder al elemento del diccionario

print(lista_de_diccionarios[0].get('edad'))

# Recorrer los elementos de la lista

for diccionario in lista_de_diccionarios:
    print(diccionario.get('nombre'))
    print(diccionario.get('apellido'))
    print(diccionario.get('direccion').get('calle'))
    print(diccionario.get('direccion').get('numero'))

# Recorrer los elemento de la lista utilizando enumerate

for i, diccionario in enumerate(lista_de_diccionarios):
    print(f"Elemento {i+1}:")
    print(diccionario.get('nombre'))
    print(diccionario.get('apellido'))
    print(diccionario.get('direccion').get('calle'))
    