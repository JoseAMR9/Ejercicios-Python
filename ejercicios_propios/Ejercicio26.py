'''
Guest Management
You have a list of guests for a party. Some names are repeated because they were entered twice by mistake.
- Convert the list into a set to remove duplicates.
- Add "Sofia" to the guest list.
- Check if "Pedro" is invited.
- Remove "Carlos" from the list.
- Display the total number of guests.
'''

guests = ["Ana", "Luis", "Pedro", "Ana", "Maria", "Luis", "Carlos"]

my_set = set(guests)
my_set.add("Sofia")

if "Pedro" in my_set:
    print("Pedro is invited")
else:
    print("Pedro is not invited")

my_set.remove("Carlos")

print(f"New list: {my_set}")

print(f"Number of guests {len(my_set)}")