my_list = []

while True:
    number = int(input("Digite un numero: "))
    if number < 0:
        break
    my_list.append(number)  

print(f"\nTu lista: {my_list}")

for elements in my_list:
    if elements > 10:
        print(f"{elements} es mayor que 10")
    else:
        print(f"{elements} es menor o igual que 10")
