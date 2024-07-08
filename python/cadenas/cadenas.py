# Programa Python usa intérprete 3.12.5

# Cadenas en Python -----------------------------------------------------------------

# Las cadenas en Python se encuentran entre comillas simples o dobles

mi_cadena = "esta es la cadena de texto"

# salto de línea \n

mi_cadena_con_salto_de_linea = "esta es la cadena de texto\ncon salto de línea"

# Cadena multilinea utilizando triple comillas y tabulación

mi_cadena_multilinea = """
\t\testa es una cadena de texto
con salto de línea
y también puede contener
varias líneas
"""

# Operaciones con cadenas -----------------------------------------------------------------

# Concatenación

primer_nombre = "Juan"
apellido = "Perez"

nombre_completo = primer_nombre + " " + apellido

# Repetición

mi_cadena_repetida = mi_cadena * 3

# Indexación

mi_cadena_indexada = "Hola, mundo!"

primera_letra = mi_cadena_indexada[0]
ultima_letra = mi_cadena_indexada[-1]

# Slicing

mi_cadena_slicada = mi_cadena_indexada[0:5]

# Métodos

mi_cadena_minusculas = mi_cadena_indexada.lower()
mi_cadena_mayusculas = mi_cadena_indexada.upper()
mi_cadena_longitud = len(mi_cadena_indexada)

# Resultados    

mi_cadena, mi_cadena_con_salto_de_linea, mi_cadena_multilinea, nombre_completo, mi_cadena_repetida, primera_letra, ultima_letra, mi_cadena_slicada, mi_cadena_minusculas, mi_cadena_mayusculas, mi_cadena_longitud

mensaje = 'Hola Mundo'
minuscula = mensaje.lower()
mayuscula = mensaje.upper()
print(mensaje, minuscula)
print(mayuscula, minuscula)