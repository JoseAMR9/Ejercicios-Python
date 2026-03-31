a = int(input("a -> "))
b = int(input("b -> "))

a , b = b , a
print(f"Nuevo valor de a: {a}")
print(f"Nuevo valor de b: {b}")

'''
aux = a
a = b
b = aux

print(f"Nuevo valor de a: {a}")
print(f"Nuevo valor de b: {b}")
'''