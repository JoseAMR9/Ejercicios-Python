'''
Unpacking
You have this list: data = [2005, "Lima", 1.75, "Engineering"]
Unpack it into 4 variables with descriptive names
Print a sentence using those variables, for example: "He/She was born in 2005, lives in Lima..."
'''
data = [2005, "Lima", 1.75, "Engineering"]

birth_year, city, height, faculty = data
print(f"He was born in {birth_year}, lives in {city}, his height is {height} and he is studying {faculty}")