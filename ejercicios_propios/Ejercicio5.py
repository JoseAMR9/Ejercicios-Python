n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
n3 = int(input("Digite el tercer numero: "))

if n2 < n1 > n3:
    print(f"{n1} es el mayor")
elif n1 < n2 > n3:
    print(f"{n2} es el mayor")
elif n1 < n3 > n2:
    print(f"{n3} es el mayor")
else:
    print("Algunos numeros son iguales")