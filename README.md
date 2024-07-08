# Programación - Python, Java, C/C++

Programación en los lenguajes: Python, Java, C y C++

- [Programación - Python, Java, C/C++](#programación---python-java-cc)
  - [Python v3](#python-v3)
    - [Variables en Python](#variables-en-python)
    - [Cadenas en Python](#cadenas-en-python)
      - [Métodos de cadena en Python](#métodos-de-cadena-en-python)
      - [Formatos de cadena en Python](#formatos-de-cadena-en-python)
      - [Concatenación de cadenas en Python](#concatenación-de-cadenas-en-python)
      - [Interpolación de cadenas en Python](#interpolación-de-cadenas-en-python)
    - [Entrada de datos por consola en Python](#entrada-de-datos-por-consola-en-python)

## Python v3

**Python 3.12.5** es el intérpetre actualmente instalado en W11. Se requiere instalar PyCharm es un IDE para Python. La versión gratuita es la Community Edition.

Programa de Python:

```python
# Programa Python con intérprete 3.12.5
print('Hola Mundo en Python con intérprete 3.12.5')
```

### Variables en Python

Las variables es un espacio de memoria, donde se almacena información. La manera de definir una variable en Python es: **nombre_variable = valor_asignado**. Se pueden almacenar valores tipo: números _enteros_, números _reales_, _letras_, _palabras_. Los valores dentro del tipo de dato, pueden cambiar.

Las variables en Python:

- Solo pueden empezar por letra o por guion bajo.
- Pueden continuar con letras, números o guion bajo.
- Sensible a mayúsculas y a minúsculas.
- No se pueden utilizar palabras reservadas.
  
```python
# Asignación de valores a variables
mi_entero = 10          # tipo int 
mi_flotante = 5.7       # tipo float
mi_cadena = 'Juan'      # tipo str (string). se puede usar comilla doble o simple 
```

Las buenas prácticas en Python:

- Comenzar con letra en minúsculas.
- Usar notación _snake_case_ (usa guión bajo entre palabras).
- Usar notación _camel case_. Esta opción no es recomendable en Python.
- La notación de Pascal, comineza con una letra en mayúsculas. No es recomendable.

### Cadenas en Python

Las cadenas en Python se encuentran entre comillas simples o dobles. Son inmutables, es decir no pueden cambiar de valor los elementos del array.

```python
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
```

Operaciones con cadenas:

```python
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
```

#### Métodos de cadena en Python

```python
# Métodos
mensaje 0 'Hola Mundo'
mi_cadena_minusculas = mensaje.lower() # minúsculas
mi_cadena_mayusculas = mensaje.upper() # mayúsculas
mi_cadena_longitud = len(mensaje)      # longitud
```

#### Formatos de cadena en Python

```python
# Formato de cadenas en Python
    var_hola = 'Hola'
    var_mundo = 'Mundo'

    print(var_hola, var_mundo)
```

#### Concatenación de cadenas en Python

```python
# Concatenación => unir dos o más cadenas en Python 
# Se utiliza el operador +

    var_hola = 'Hola'
    var_mundo = 'Mundo'
    var_concatenada = var_hola + " " + var_Mundo
```

#### Interpolación de cadenas en Python

```python
# Interpolación. Se usa la letra f

    var_hola = 'Hola'
    var_mundo = 'Mundo'
    var_interpolada = f'Mi cadena: {var_hola} {var_mundo}'
```

```python
# Interpolación con triple comillas (simples o dobles)

    var_hola = 'Hola'
    var_mundo = 'Mundo'
    var_interpolada = f'''Mi cadena: 
        {var_hola} 
        {var_mundo} '''
    # Imprime en multilínea. Acepta un formato de tabulación y de salto de línea
```

### Entrada de datos por consola en Python

La entrada de datos por consola en Python utiliza la instrucción `input()`.

```python
    print("Ingrese un mensaje:")
    entrada = input()

    print(f'El dato introducido por consola es: {entrada}')
```

Para que el operador **+** realice la suma y no la concatenación de dos números, se debe convertir el tipo de dato introducido (string) a tipo entero.

```python
# int() -> convierte una cadena a un tipo entero
# float() -> convierte una cadena a un tipo decimal

    numero1 = int(input('Intro el primer número: '))
    numero2 = int(input('Intro el segundo número: '))
    suma = numero1 + numero2    #La conversión a int() se puede realizar aquí

    print(f'El Resultado de {numero1} + {numero2} = {suma}')
```
