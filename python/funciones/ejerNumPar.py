# Crear una función llamada es_numero_par

def es_numero_par(numero):
    """
    Esta función recibe un número entero como entrada y devuelve True si el número es par y False si no lo es.

    Parámetros:
    numero (int): El número a evaluar

    Devuelve:
    bool: True si el número es par, False si no lo es
    """
    # Verificar si el número es par
    if numero % 2 == 0:
        return True
    else:
        return False

# Prueba la función con algunos valores

print(es_numero_par(10))  # Devuelve True
print(es_numero_par(9))   # Devuelve False
print(es_numero_par(-10))  # Devuelve True
print(es_numero_par(-9))   # Devuelve False
print(es_numero_par(0))   # Devuelve True