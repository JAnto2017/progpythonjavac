# Listas en Python

# Preguntar si un valor existe en mi lista

mi_lista = [1, 2, 3, 4, 5]

valor_buscado = 3

if valor_buscado in mi_lista:
    print(f"El número {valor_buscado} se encuentra en la lista.") 
    
    # Preguntar si un valor existe en mi lista y retornar su posición
    
    posicion = mi_lista.index(valor_buscado)
    print(f"La posición de {valor_buscado} es {posicion}.")
else:
    print(f"El número {valor_buscado} no se encuentra en la lista.")
    