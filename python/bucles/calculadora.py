# Calculadora en Python
# Menú con las opciones de: suma, resta, multiplicación, división, salir
# Usuario introduce las opciones de selección
# Los valores de operación deben ser números decimales

def menu():
    print("\nMenú de operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: División por cero")
        return None
# ----------------------------------------------------------------
opcion = operando1 = operando2 = 0
salir = False
while not salir:
    menu()
    opcion = int(input("Escoje una opción: "))
    
    if 1 <= opcion <= 4:    # opcion >= 1 and opcion <= 4
        operando1 = float(input('Operando 1: '))
        operando2 = float(input('Operando 2: '))
        
    if opcion == 1:
        print(f'Resultado de la suma: {suma(operando1,operando2):.2f}\n')   
    elif opcion == 2:
        print(f'Resultado de la resta: {resta(operando1,operando2):.2f}\n')
    elif opcion == 3:
        print(f'Resultado de la multiplicación: {multiplicacion(operando1,operando2):.2f}\n')
    elif opcion == 4: 
        resultado = division(operando1, operando2)
        if resultado is not None:
            print(f'Resultado de la división: {resultado:.2f}\n')
    elif opcion == 5:
        salir = True
        print("Saliendo del programa...\n")
    else:
        print("Opción incorrecta. Intente nuevamente.\n")