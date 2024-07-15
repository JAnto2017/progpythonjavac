# Calculadora en Python con funciones
# 1. mostrar el menú usando una función.
# 2. solicitar los valores de los operadores en una función
# 3. la operación a ejecutar va en otra función por separado

# crear función que muestre el menú: suma, resta, multiplicación, división y salir

def menu():
    print("Calculadora en Python")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("Ingrese su opción: ")
    return int(input())

# crear función para sumar dos números

def suma(a, b):
    return a + b

# crear función para restar dos números

def resta(a, b):
    return a - b

# crear función para multiplicar dos números

def multiplicacion(a, b):
    return a * b

# crear función para dividir dos números

def division(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero")
        return None
    return a / b

# crear función para solicitar los valores 

def pedir_valores():
    num1 = float(input("Ingrese el primer operando: "))
    num2 = float(input("Ingrese el segundo operando: "))
    return num1, num2


# mostrar los valores ingresados
# print("Los valores ingresados son:", num1, "y", num2)

# realizar las operaciones
# ciclo para mostrar el menú y realizar las operaciones

salir = False
while not salir:
    opcion = menu()
    resultado = 0.0
    num1 = 0.0
    num2 = 0.0
    if 1 <= opcion <= 4:
        # pedir los valores al usuario
        num1, num2 = pedir_valores()
        
    if opcion == 5:
        print("Saliendo...")
        salir = True
    
    elif opcion == 1:
        #num1 = float(input("Ingrese el primer número: "))
        #num2 = float(input("Ingrese el segundo número: "))
        resultado = suma(num1, num2)
        print(f"El resultado {num1} + {num2} = {resultado}\n")
    
    elif opcion == 2:
        #num1 = float(input("Ingrese el primer número: "))
        #num2 = float(input("Ingrese el segundo número: "))
        resultado = resta(num1, num2)
        print(f"El resultado {num1} - {num2} = {resultado}\n")
    
    elif opcion == 3:
        #num1 = float(input("Ingrese el primer número: "))
        #num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion(num1, num2)
        print(f"El resultado {num1} * {num2} = {resultado}\n")
    
    elif opcion == 4:
        #num1 = float(input("Ingrese el dividendo: "))
        #num2 = float(input("Ingrese el divisor: "))
        resultado = division(num1, num2)
        print(f"El resultado {num1} / {num2} = {resultado}\n")
    else:
        print("Opción inválida")
        

