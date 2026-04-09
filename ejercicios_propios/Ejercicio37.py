grades = int(input("Enter your final grade: "))

if 90 < grades <= 100:
    print("A")
elif 80 < grades < 89:
    print("B")
elif 70 < grades < 79:
    print("C")
elif 60 < grades < 69:
    print("D")
else:
    print("F")