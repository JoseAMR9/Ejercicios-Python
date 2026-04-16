datos = {"a": 2, "b": 5, "c": 8, "d": 11}

for elements in datos.values():
    if elements % 2 == 0:
        print(f"Par {elements}")
    else:
        continue
else:
    print("Recorrido completado")