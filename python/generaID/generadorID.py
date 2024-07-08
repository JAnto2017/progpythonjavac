# Programa Python 3.12.5
# Pide el Nombre ?
# Pide el Apellido ?
# Pide el Año ?
# Extraer los dos primeros caracteres del Nombre
# Extraer los dos primeros caracteres del Apellido
# Extraer los dos últimos caracteres del Año
# Generar un número aleatorio de 4 dígitos
# Concatenar las extracciones anteriores y el número aleatorio

from random import randint


print('*** Sistema de Generador ID ***')

nombre = input("Introduce tu nombre: ").upper()

apellido = input("Introduce tu apellido: ").upper()

anio = input("Introduce tu año de nacimiento (YYYY): ") # los valores se ingresan como cadena de texto

nombre_cortado = nombre[:2]

apellido_cortado = apellido[:2]

anio_cortado = anio[-2:]

# Genera un número de 4 dígitos aleatorio

aleatorio = randint(0,9999)

# Generar el ID único con interpolación

nombre_apellido_anio_alea = f'{nombre_cortado}{apellido_cortado}{anio_cortado}{aleatorio}'

# Generar el ID único con concatenación de cadenas

# nombre_apellido_anio_alea = nombre_cortado + apellido_cortado + anio_cortado + str(aleatorio)

# Mostrar el ID único generado

print(f'''\nHola {nombre}, tu número
      de identificación ID generado
      por el sistema es:
      {nombre_apellido_anio_alea}''')