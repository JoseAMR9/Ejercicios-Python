lista1 = ["juan","jose","pablo","marco","antonio"]
lista2 = ["pedro","jose","marco","julio","ana","josue"]

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(f"\nLista de palabras de las dos listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {soloA}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {soloB}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")