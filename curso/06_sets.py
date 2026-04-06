
my_set = set() #primera forma de declarar un set
my_other_set = {"Jose", "Marcelo", 18} #segunda forma de declarar un set

my_other_set.add("Perú") # un set no es una estructura ordenada, agrega el elemento en cualquier lugar y ademas no permite repetidos
print(my_other_set)

print("Jose" in my_other_set) # buscar datos en los sets
print("Josue" in my_other_set)

my_other_set.remove("Marcelo") # eliminar un dato del set
print(my_other_set)

my_other_set.clear() # eliminar todos los datos del set
print(my_other_set)

del my_other_set # eliminar por completo el set (ya no lo podremos utilizar)

my_set = {"Jose", "Marcelo", 18}
my_set2 = {"C++", "Python"}

my_new_set = my_set.union(my_set2) # uniendo dos sets
print(my_new_set)

print(my_new_set.difference(my_set)) # Devuelve un nuevo set con los elementos de my_new_set que no están en my_set.


