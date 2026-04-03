'''
Access and Slicing
Given the list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], obtain:
- The first 3 elements
- The last 3 elements
- The elements at even positions (index 0, 2, 4...)
- The reversed list using slicing (without using .reverse())
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_3_elements = my_list[:3] # == my_list[0:3]
last_3_elements = my_list[-3:]
elements_even_position = my_list[0::2] # -> my_list[0:10:2]
reverse_list = my_list[::-1]

print(f"First 3 elements in list: {first_3_elements}")
print(f"Last 3 elements in list: {last_3_elements}")
print(f"Elements in even positions in list: {elements_even_position}")
print(f"Reversed list: {reverse_list}")