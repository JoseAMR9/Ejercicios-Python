class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self, user, password):
        return self.__username == user and self.__password == password
    
    def change_password(self, new_password):
        self.__password = new_password
    
    def show_info(self):
        print(f"Username: {self.__username}")
        print(f"Password: {self.__password}")

user = input("Enter your username: ")
password = input("Enter your password: ")

user1 = User(user, password)

print("\nLOGIN: ")
user = input("Enter your username: ")
password = input("Enter your password: ")

if user1.login(user,password):
    print("Login succesfully")
else:
    print("Wrong user or password")

print("\nCHANGE PASSWORD: ")
new_password = input("Enter your new password: ")
user1.change_password(new_password)

user1.show_info()


