try:
    grades = {
        "Ana": 18,
        "Luis": 15,
        "Carlos": 20
    }
    student = input("Enter the name of one student: ")
    print(grades[student])
except KeyError:
    print("Student not found")