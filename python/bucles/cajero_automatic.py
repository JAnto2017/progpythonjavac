# Cajero Automático

print('*** CAJERO AUTOMÁTICO ***')

saldo = 1000 # saldo inicial
salir = False

while not salir:
    print('\nMenú:')
    print('1. Ingresar dinero')
    print('2. Retirar dinero')
    print('3. Consultar saldo')
    print('4. Salir')
    
    opcion = int(input('Elija una opción: '))
    
    if opcion == 1:
        cantidad = float(input('Ingrese la cantidad de dinero a ingresar: '))
        saldo += cantidad
        print(f'Dinero ingresado correctamente. Nuevo saldo: ${saldo:.2f}')
    
    elif opcion == 2:
        cantidad = float(input('Ingrese la cantidad de dinero a retirar: '))
        if cantidad <= saldo:
            saldo -= cantidad
            print(f'Dinero retirado exitosamente. Nuevo saldo: ${saldo:.2f}')
        else:
            print('Saldo insuficiente.')
    
    elif opcion == 3:
        print(f'Su saldo actual es: {saldo:.2f}€')  # formato de números reales
    
    elif opcion == 4:
        print('Gracias por utilizar nuestro cajero automático.')
        salir = True
    else:
        print('Opción incorrecta. Intente nuevamente.\n')
        
