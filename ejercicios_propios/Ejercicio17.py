'''
Manipulation
Create a list with the names of 5 friends. Then:
- Add a new friend to the end
- Insert another friend at position 2
- Remove the third element
- Sort the list alphabetically
'''
friend_list = ["Pepe", "Maria", "Pedro", "Marco", "Carla"]

friend_list.append("Harvey") # -> [..., "Marco", "Carla", Harvey]
friend_list.insert(2,"Jessica") # -> [..., "Maria", "Jessica", "Pedro", "Marco", "Carla", Harvey]
friend_list.pop(2) # -> ["Pepe", "Maria", "Pedro", "Marco", "Carla", Harvey]
friend_list.sort()
print(friend_list)