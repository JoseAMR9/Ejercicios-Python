'''
Without Methods, Only Logic
Given the list [3, 1, 4, 1, 5, 9, 2, 6], without using .sort() or built-in functions:
- Find the maximum value
- Find the minimum value
- Calculate the sum of all elements
'''
num_list = [3, 1, 4, 1, 5, 9, 2, 6]

max_number = num_list[0]
min_number = num_list[0]
sum_elements = 0
for numbers in num_list:
    if numbers > max_number:
        max_number = numbers
    if numbers < min_number:
        min_number = numbers
    sum_elements += numbers

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
print(f"Total sum: {sum_elements}")