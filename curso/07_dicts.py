
my_dict = dict()
my_other_dict = {"Nombre" : "Jose", "Apellido" : "Marcelo", "Edad" : 18}

my_dict = {
    "Nombre" : "Jose",
    "Apellido" : "Marcelo",
    "Edad" : 18,
    "Languages" : {"Python", "C++"}
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pepe"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle jose" # agregar un nuevo elemento al diccionario
print(my_dict)

del my_dict["Calle"] # eliminando el elemento "Calle"
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", "Apellido")) # crea un dict nuevo con las claves "Nombre" y "Apellido" y sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys((my_dict)) # crea un dict nuevo con las claves de my_dict, sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Jose")# crea un dict nuevo con las claves de my_dict y los valores "Jose"
print((my_new_dict))