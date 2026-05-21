class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
    
    def show_info(self):
        print(f"\nName: {self.__name}")
        print(f"Grade: {self.__grade}")

    def is_approved(self):
        return self.__grade >= 11

    def get_name(self):
        return self.__name
    def get_grade(self):
        return self.__grade
    
name = input("Enter your name: ")
grade = int(input("Enter your final grade: "))

student1 = Student(name,grade)
student1.show_info()

print(student1.get_name())
print(student1.get_grade())

if(student1.is_approved()):
    print("YOU PASSED")
else:
    print("YOU FAILED")
