students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Charlie", 78, 21),
    (104, "David", 88, 20)
]

top_student = max(students, key=lambda x: x[2])
print(f"Student with the Highest Grade:\n- {top_student[1]} (Grade: {top_student[2]})")

name_grade_list = [(name, grade) for (_, name, grade, _) in students]
print("\nName-Grade List:")
for name, grade in name_grade_list:
    print(f"- {name}: {grade}")

print("\nTuple Immutability Demonstration:")
try:
    students[0][2] = 95
except TypeError as e:
    print("Error:", e)
    print("\nExplanation:")
    print("Tuples are immutable, meaning their values cannot be changed once assigned.")
    print("They are preferred for fixed data like student records to ensure data integrity.")
