try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Is even")
    else:
        print("Is odd")
except ValueError:
    print("Invalid number")
finally:
    print("Program finished")
