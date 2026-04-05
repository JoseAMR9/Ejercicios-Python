'''
Create a tuple with the data of a student: name, age, average, and major. Then print each value using indices, show how many elements the tuple has, and print the data in reverse order.
'''

my_tuple = ("Jose", 18, 16.8, "Engineering")

for data in my_tuple:
    print(data, end= " ")

print(f"\nLenght of tuple: {len(my_tuple)}")
print("Reversed tuple:", my_tuple[::-1])