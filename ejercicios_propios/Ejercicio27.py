'''
Merge the two sets into one called all_languages.
Use .difference() to find which languages Team A knows that Team B does not.
Do the same in reverse: find what Team B knows that Team A does not.
'''

team_a = {"Python", "Java", "C++"}
team_b = {"JavaScript", "Python", "Ruby"}

all_languages = team_a.union(team_b)
print(all_languages)

print(f"Difference between team A and team B: {team_a.difference(team_b)}")
print(f"Difference between team B and team A: {team_b.difference(team_a)}")