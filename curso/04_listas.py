## Lists ##

my_list = [1,5,4,2,10,7]
my_list2 = [17, 1.81, "Pepito", "Alcantara"]

print(len(my_list2))
print(my_list2)
print(my_list2[0])

age, height, name, surname = my_list2
print(name)

my_list2.append("Romero") # agregar a la ultima posicion
my_list2.insert(3, "Alejandro") # insertar en una posicion especifica
# my_list2.reverse() -> invierte la lista 

my_list.remove(10) # elimina un elemento
my_list.pop() # elimina el ultimo elemento (tambien puedes poner el indice de un elemento)
del my_list[2] # elimina el elemento [i]
my_list.clear() # elimina todos los elementos
# my_list.sort() -> ordena la lista
# my_list[1:6:2] -> my_list[inicio, fin, paso]

print(my_list2)
print(my_list)