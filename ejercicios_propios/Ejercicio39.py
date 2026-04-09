user = input("Enter your username: ")
password = input("Enter your password: ")

if user == "admin" and password == "1234":
    print(f"Welcome {user}")
else:
    print("Wrong username or password")
