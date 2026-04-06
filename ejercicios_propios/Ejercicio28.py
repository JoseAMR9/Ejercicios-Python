'''
Separate the words using .split().
Convert them into a set to get only the unique words.
Display how many unique words there are.
Check if the word "cat" is in the set.
'''

frase = "el gato come pescado y el perro come carne y el gato duerme".split()

my_set = set(frase)

print(f"Unique words: {len(my_set)}")

if "gato" in my_set:
    print("Gato is in the set")
else:
    print("Gato is not in the set")