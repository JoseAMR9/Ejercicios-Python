def sum_numbers(*number):
    total = 0
    for n in number:
        total += n
    return total

result = sum_numbers(1,2,3,4,5,6,7,8,9,10)
print(result)