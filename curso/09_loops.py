my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es mayor o igual que 10")

while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)


my_list = [1,5,4,2,10,7]

for element in my_list:
    print(element)
else:
    print("El bucle for ha finalizado")

my_other_dict = {"Nombre" : "Jose", "Apellido" : "Marcelo", "Edad" : 18}

for element in my_other_dict.values():
    print(element)
    if element == "Marcelo":
        continue
    print("Se ejecuta")
else:
    print("El bucle for del diccionario a finalizado")
