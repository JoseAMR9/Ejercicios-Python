try:
    num1 = int(input("Enter the number one: "))
    num2 = int(input("Enter the number two: "))
    print(f"The division is: {num1 / num2}")
except(ZeroDivisionError, ValueError):
    print("ERROR")
else:
    print("Compiled succesfully")