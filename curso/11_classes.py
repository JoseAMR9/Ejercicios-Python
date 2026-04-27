class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
        self.__name = name
        self.__surname = surname

    def walk(self):
        print(f"{self.full_name} esta caminando")

    def getName(self):
        return self.__name
    def getSurname(self):
        return self.__surname

my_person = Person("Jose", "Marcelo")
print(my_person.full_name)
my_person.walk()

print(my_person.getName())
print(my_person.getSurname())