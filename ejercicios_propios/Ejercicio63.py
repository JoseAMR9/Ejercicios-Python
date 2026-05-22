'''
file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()
'''
try:
    with open("data,txt", "r") as file: # with cierra el archivo automaticamente
        print(file.read())
except FileNotFoundError:
    print("File not found")