# Determinar si un número es positivo haciendo uso del if - elif - else
# Solicitar número al usuario
# Determinar si el número mayor que 0
# Si es True imprimir 'número es positiov'
# Si es False determinar si el número es menor que 0
# Si es menor que 0 imprimir 'número negativo'
# Si es False el número es igual a 0.

numero = int(input("Ingrese un número: "))

if numero > 0:
    print("número es positivo")
elif numero == 0:
    print("número es igual a 0")
elif numero < 0:
    print("número es negativo")
