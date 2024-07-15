# Argumentos variables en Python

# Crear una función que reciba argumentos variables
from math import prod


def suma_variables(*args):
    # Recorrer los argumentos y sumarlos
    return sum(args)

# Utilizar la función con diferentes argumentos
print(suma_variables(1, 2, 3, 4, 5))  # Imprime: 15
print(suma_variables(10, 20, 30))  # Imprime: 60
print(suma_variables(5, 10, 15, 20))  # Imprime: 50
print(suma_variables(5,8)) # Imprime: 13

def mi_funcion(nombre, *args):
    print(f"Hola {nombre}! Mi suma es: {suma_variables(*args)}")

mi_funcion("Juan", 1, 2, 3, 4, 5)  # Imprime: Hola Juan! Mi suma es: 15

# crear función que utiliza **keywards

def multiplica_variables(**kwargs):
    # Recorrer los argumentos y multiplicarlos
    return prod(kwargs.values())

print(multiplica_variables(a=2, b=3, c=4))  # Imprime: 24

def mi_funcion_kwargs(nombre, **kwargs):
    print(f"Hola {nombre}! Mi multiplica es: {multiplica_variables(**kwargs)}")

mi_funcion_kwargs("Juan", a=2, b=3, c=4)  # Imprime: Hola Juan! Mi producto es: 24