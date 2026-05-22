try:
    names = ["Ana", "Luis", "Carlos", "Elena", "Mario"]
    pos = int(input("Enter a position: "))
    print(names[pos])
    
except IndexError:
    print("ERROR: Invalid position")

except ValueError:
    print("ERROR: Enter only numbers")
