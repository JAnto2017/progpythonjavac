# Crear una función con argumentos o parámetros

# Función que recibe parámetros y los imprime
def saludar(parametro):
    print(f'Mensaje recibido por parámetros: {parametro}')
# Llamada a la función
saludar('Hola Mundo')

# 1. Definir la función

def suma_numeros(*args):
    # 2. Utilizar la función con argumentos (*args) para sumar todos los números
    return sum(args)

# 2. Llamar a la función

suma = suma_numeros(1, 2, 3, 4, 5)

# 3. Imprimir la función

print(suma)
