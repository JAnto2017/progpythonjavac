# Menú interactiva con ciclo WHILE

salir = False;

while not salir:
    print(f'''Menú:
        1. Crear cuenta
        2. Eliminar cuenta
        3. Salir  
    ''')

    opcion = int(input('Elegir opción: '))

    if opcion == 1:
        print('Creando cuenta...\n')
    elif opcion == 2:
        print('Eliminando cuenta...\n')
    elif opcion == 3:
        print('Saliendo...\n')
        salir = True
    else:
        print('Opción inválida. Intente nuevamente.\n')