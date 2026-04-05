# Diferencia entre listas -> no se puede modificar ni eliminar elementos(inmutable) / 
my_tuple = tuple()
my_tuple = (18, 1.81, "Jose", "Marcelo")
my_tuple2 = (10,20,30,40)

print(my_tuple)
print(my_tuple[0])
print(my_tuple[::-1])
print(my_tuple.count("Jose"))
print(my_tuple.index("Marcelo"))

# my_tuple[0] = 20 -> ERROR
# del my_tuple -> ERROR

print(my_tuple + my_tuple2)

my_tuple2 = list(my_tuple2)
print(my_tuple2)
