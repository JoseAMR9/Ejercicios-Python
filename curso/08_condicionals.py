my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 2

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


my_string = ""

if not my_string: # -> se cumple si el string esta vacio
    print("Mi cadena de texto esta vacia")

if my_string == "Mi cadena de texto":
    print("Estas cadenas coinciden")

print("La ejecucion continua")