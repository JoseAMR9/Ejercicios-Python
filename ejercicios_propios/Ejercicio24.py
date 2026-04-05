'''
Nested tuples
Create a tuple that represents a 3x3 board (a tuple containing 3 tuples). Access and print the center element, the entire second row, and the last element of the first row.
'''

my_tuple = ((1,2,3), (4,5,6), (7,8,9))
print(f"Center element: {my_tuple[1][1]}")
print(f"Second row: {my_tuple[1]}")
print(f"Last element of the first row: {my_tuple[0][-1]}")