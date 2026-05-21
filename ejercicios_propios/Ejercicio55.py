class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author  
        self.__available = True

    def borrow(self):
        if not self.__available:
            print("Book is already borrowed")
            return
        self.__available = False

    def return_book(self):
        if self.__available:
            print("Book is already available")
            return
        self.__available = True

    def show_info(self):
        print(f"\nTitle: {self.__title}")
        print(f"Author: {self.__author}")
        status = "Yes" if self.__available else "No"
        print(f"Available: {status}")

book1 = Book("Las Brujas", "Jose Marcelo")

book1.show_info()

book1.borrow()

book1.show_info()

book1.return_book()

book1.show_info()