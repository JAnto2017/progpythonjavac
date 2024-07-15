# SET en Python

# Set de nombres en Python

# Los conjuntos en Python son colecciones desordenadas de elementos únicos.
# No se pueden repetir los elementos del Set == Conjuntos en Python

# Creación de un Set vacío

s = set()

# Añadir elementos al Set

s.add(1)
s.add(2)
s.add(3)

# Mostrar el Set

print(s)

# imprimir los elementos del Set usando el bucle for

for num in s:
    print(num, end='')

# Verificar si un elemento está en el Set

print("\nEl número 2 está en el Set?", 2 in s)

# Obtener la longitud de los elementos del Set

print("\nLongitud del Set:", len(s))

# crear un set de elemetos de diferente tipo

s2 = {1, "hola", 3.14}

# concatenar dos sets

s3 = s.union(s2)

# mostrar el nuevo Set

print("\nSet concatenado:", s3)

# eliminar un elemento del set

s.remove(2)

# mostrar el Set después de eliminar un elemento

print("\nSet después de eliminar el número 2:", s)