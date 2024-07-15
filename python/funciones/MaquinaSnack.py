# Proyecto de Máquina de Snaks

# Definir elementos del diccionario

snacks = [
    {'id':0, 'nombre':'Papas', 'precio':30}, 
    {'id':1, 'nombre':'Refresco', 'precio': 50}, 
    {'id':2, 'nombre':'Sandwich', 'precio': 120}]

# Definir lista de productos (listas)

productos = []

# Programa principal

print("---- Productos ----")
print('Snacks disponibles:')
for snack in snacks:
    print(f'\tId: {snack["id"]} '
          f'-> {snack["nombre"]}'
          f' - Precio: ${snack["precio"]}')

# funcción que recibe: snacks disponibles y productos

def maquina_snacks(snacks, productos):
    salir = False
    while not salir:
        print("\n\t---- Menu ----")
        print("\t1. Comprar producto")
        print("\t2. Mostrar productos")
        print("\t3. Salir")
        opcion = int(input('\tEscoge una opción: '))
        if opcion == 1:
            comprar_prducto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)        
        elif opcion == 3:
            print("Adios")
            salir = True
        else:
            print("\n\tOpción inválida. Intentar de nuevo.")

# función comprar producto

def comprar_prducto(snacks, productos):
    id_snack = int(input("Ingrese el ID del producto a comprar: "))
    for snack in snacks:
        if snack['id'] == id_snack:
            precio = snack['precio']
            nombre_snack = snack['nombre']
            precio_total = precio
            agregar_producto(nombre_snack, precio_total, productos)
            print(f"Compra realizada con éxito. El producto {nombre_snack} ha sido añadido al ticket.")
            #input("Presione Enter para continuar...")
    #productos.clear()

# función agregar producto

def agregar_producto(nombre, precio, productos):
    productos.append({'nombre': nombre, 'precio': precio})
    print(f"Producto {nombre} agregado al ticket.")
    #input("Presione Enter para continuar...")
    total = sum(p['precio'] for p in productos)
    #print(f'Total a pagar: {total}€')
    input("Presione Enter para continuar...")
    
# función mostrar ticket

def mostrar_ticket(productos):
    print("\n---- Ticket ----")
    for producto in productos:
        print(f'\tProducto: {producto["nombre"]}'
              f' - Precio: {producto["precio"]}€')
        #print(f'\tTotal: {producto["precio"]}€')
    
    print("-------------------------------")
    total = sum(p['precio'] for p in productos)
    print(f'Total a pagar: {total}€')
    input("Presione Enter para continuar...")
    productos.clear()
        
# Llamada a la función principal

maquina_snacks(snacks, productos)