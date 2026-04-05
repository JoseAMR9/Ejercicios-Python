'''
Create a tuple with 8 numbers where some values are repeated: (3, 7, 2, 7, 5, 3, 7, 1). Find how many times the number 7 appears, determine the position of the number 5, and print only the first 4 elements using slicing.
'''

my_tuple = (3, 7, 2, 7, 5, 3, 7, 1)
print(f"Number 7 appers: {my_tuple.count(7)} times")
print(f"Position of the number 5: {my_tuple.index(5)}")
print(f"First 4 elements: {my_tuple[:4]}")