# Calcular el área de un rectángulo
# Creacion de la variable base con el valor numerico de 5
# Creacion de la variable altura con el valor numerico de 10
# Creacion de la variable area_resultado, y almacena al calculo del area del rectangulo
# Impresion del resultado del programa con el calculo del area

base = 5
altura = 10

area_resultado = base * altura

print(f"El área del rectángulo es: {area_resultado}")

# Contador de vocales 
# Declarar la variable
# Agregar el ciclo for 
# Contar el número de vocales
# Imprimir la cantidad de vocales encontradas en la cadena

cadena = 'Hola Mundo'
contador = 0
for letra in cadena:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        contador = contador + 1

print(f"La cadena tiene {contador} caracteres.")