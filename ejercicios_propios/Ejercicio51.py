class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def show_info(self):
        print(f"\nBrand: {self.__brand}")
        print(f"Model: {self.__model}")
        print(f"Age: {self.__year}")

car1 = Car("Mercedes", "AMG", 2024)
car2 = Car("Audi", "R8", 2024)

car1.show_info()
car2.show_info()