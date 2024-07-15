# Tupla en Python

# tupla de nombres

nombres = ('Juan', 'Pedro', 'Maria', 'Isabel')
print(f'Tupla inmutable de nombres: {nombres}')

# tupla heterogénea

heterogenea = (10, 'Hola', True, [1, 2, 3])
print(f'Tupla heterogénea: {heterogenea}')

# En las tuplas, los paréntesis son opcionales

tupla_sin_parentesis = 10, 'Hola', True, [1, 2, 3]
print(f'Tupla sin paréntesis: {tupla_sin_parentesis}')

# En las tuplas, los valores que terminan en coma, sin paréntesis son opcionales

tupla_con_valor_coma = 10, 'Hola',
print(f'Tupla con valor final en coma: {tupla_con_valor_coma}')

# recorrer los elementos de una tupla

for nombre in nombres:
    print(nombre)
