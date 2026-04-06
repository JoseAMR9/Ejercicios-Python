'''
Find the subjects that both students have in common
Find the subjects that only student 1 takes and not student 2.
Find all the subjects between both students without duplicates.
'''

student1 = {"Matematica", "Historia", "Fisica", "Arte"}
student2 = {"Fisica", "Quimica", "Arte", "Literatura"}

print(f"Subjects in common: {student1.intersection(student2)}")
print(f"Subjects that only student1 takes and not student: {student1.difference(student2)}")
print(f"All subjects (no duplicates): {student1.union(student2)}")