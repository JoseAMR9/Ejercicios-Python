import os

class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    
    def show_info(self):
        return f"{self.__name}: ${self.__price}"

class Cart:
    def __init__(self):
        self.__products = []
    
    def add_product(self, product):
        self.__products.append(product)
    
    def total_price(self):
        total = 0
        for product in self.__products:
            total += product.get_price()
        return total

    def show_cart(self):
        print("\nCART:")
        for product in self.__products:
            print(product.show_info())

def clear():
    os.system("cls")

def pause():
    input("\nPress ENTER to continue...")

cart1 = Cart()
while True:
    clear()
    print("1.- Add product to your cart")
    print("2.- Show your cart")
    print("3.- Exit")
    try:
        option = int(input("Option: "))
    except:
        print("Invalid option")
        pause()
        continue
    match(option):
        case 1:
            clear()
            name = input("\nName: ")
            price = float(input("Price: "))
            product1 = Product(name,price)
            cart1.add_product(product1)
            pause()
        case 2:
            clear()
            cart1.show_cart()
            if cart1.total_price() > 100:
                print("\nYOU HAVE A DISCOUNT (30%)")
                discount = cart1.total_price() * 0.30
                print(f"DISCOUNT: {discount}")
                print(f"TOTAL PRICE: {cart1.total_price() - discount}")
            else:
                print(f"TOTAL PRICE: {cart1.total_price()}")
            pause()
        case 3:
            break