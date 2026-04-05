'''
Unpacking
Create a tuple with 5 cities. Using unpacking, assign the first city to one variable, the middle cities to another variable as a list, and the last city to another variable. Print each variable separately.
'''

my_tuple = ("Lima", "Arequipa", "Trujillo", "Cusco", "Chiclayo")
a, *b, c= my_tuple

print(a)
print(b)
print(c)