class Library:
    def __init__(self):
        self.__bookList = []

    def addBook(self, book):
        self.__bookList.append(book)

    def showBooks(self):
        for book in self.__bookList:
            print(book)
    
    def book_exists(self, title):
        for book in self.__bookList:
            if(book == title):    
                return True
        return False

library1 = Library()

name = input("Name of the book: ")
library1.addBook(name)

name = input("Name of the book: ")
library1.addBook(name)

name = input("Name of the book: ")
library1.addBook(name)

print("\nBOOKS: ")
library1.showBooks()

name = input("Name of the book: ")

if library1.book_exists(name):
    print("The book exist")
else:
    print("The book does not exist")