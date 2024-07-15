# Retorno de tupla desde una función 

# definir la función que recibe parámetros y retorna una tupla
def persona_mayuscula(nombre, apellido, edad):
    print("Esta función retorna valores (tupla)")
    return (nombre.upper(), apellido.upper(), edad)

# Programa principal
nombre, apellido, edad = persona_mayuscula('Sandra','Jiménez', 43)
print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')