# Operadores Lógicos AND y OR

var_a = True
var_b = False

# AND (AND lógico): Retorna True só se ambos os operandos forem True

print("var_a and var_b => ", var_a and var_b)  # False

# OR (OR lógico): Retorna True se pelo menos um dos operandos forem True

print("var_a or var_b => ", var_a or var_b)  # True

# NOT (NOT lógico): Inverte o valor booleano

print("not var_a => ", not var_a)  # False

if (var_a and not var_b):
    print("Aqui: var_a and not var_b")
elif (not var_a and not var_b):
    print("Aqui: not var_a and not var_b")

usonot = not var_a
print("var_a: ", var_a)
print("NOT var_a: ", usonot)