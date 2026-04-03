'''
Nested Lists
Create a list that represents a small table of 3 students, where each student is itself a list with [name, age, grade]. Then:
Print the name of the second student
Print the grade of the third student
'''

student_list = [
    ["Jose", 18, 20],
    ["Mario", 16, 14],
    ["Martha", 40, 19]
]
print(student_list[1][0])
print(student_list[2][2])
