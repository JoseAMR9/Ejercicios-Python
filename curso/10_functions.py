def my_function():
    print("Esto es una función")

my_function()

def sum_two_numbers(a, b):
    print(a + b)

sum_two_numbers(10,10)

def return_sum_two_numbers(a, b):
    return a + b

my_result = return_sum_two_numbers(10,5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Marcelo", name = "Jose")
print_name("Jose", "Marcelo")

def print_name_with_default(name, surname, alias = "No tiene alias"): # -> si no se coloca el tercer parametro, como default imprime "No tiene alias"
    print(f"{name} {surname} {alias}")

print_name_with_default("Jose", "Marcelo")
print_name_with_default("Jose", "Marcelo", "Josefino9")

def print_texts(*text): # -> El * hace que puedas agregar la cantidad de textos que tu quieras
    print(text)

print_texts("Hola", "Jose", "Marcelo")