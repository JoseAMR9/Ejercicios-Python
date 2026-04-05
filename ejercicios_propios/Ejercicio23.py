'''
Concatenation and conversion
You have two tuples: one with fruits and another with vegetables. Join them into a single tuple, then convert it into a list, add a new element to the list, and finally convert it back into a tuple.
'''

my_tupleFruits = ("Apple", "Banana", "Strawberries", "Mango", "Avocado")
my_tupleVegetables = ("Tomato", "Carrot", "Lettuce", "Onion", "Potato")

my_list_FruitsAndVegetables = list(my_tupleFruits + my_tupleVegetables)
my_list_FruitsAndVegetables.append("Broccoli")

my_tuple_FruitsAndVegetables = tuple(my_list_FruitsAndVegetables)
print(my_tuple_FruitsAndVegetables)