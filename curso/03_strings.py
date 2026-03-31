my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

print("\nString con salto de linea")
print("\tString con tabulación")

name, surname, age = "José" , "Marcelo" , 18

# %s for strings, %d for integers, %f for floats
print("\nMi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
language = "Python"
a,b,c,d,e,f = language
print(a)
print(e)

#Divisiones
print("\n")
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isdigit())
print("1".isdigit())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))
