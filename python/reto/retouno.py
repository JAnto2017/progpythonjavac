# Generador de email
# Pedir el nombre del usuario y convertir en minúsculas
# Pedir el apellido del usuario y convertir en minúsculas
# Concatenar el nombre del usuario y el apellido con un punto entre ambos
# Imprimir el email creado
# Imprimit Felicidades!

def generate_email():
    name = input("Ingrese su nombre: ").lower()
    last_name = input("Ingrese su apellido: ").lower()
    dominio = 'midominio.com'
    email = f"{name}.{last_name}@{dominio}"
    print(f"Email generado: {email}")
    print("Felicidades!")

generate_email()