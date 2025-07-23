students = ["Alice", "Bob", "Charlie", "David", "Eva"]
scores = [95, 82, 91, 88, 97]


print("Numbered list of students:")
for i, student in enumerate(students):
    print(f"{i+1}. {student}")



print("\nStudents and their scores:")
for i, (student, score) in enumerate(zip(students, scores)):
    print(f"{student}: {score}")

high_scorers_indices = [i for i, score in enumerate(scores) if score > 90]
print("\nPositions of students with score > 90:", high_scorers_indices)


position_to_student = {i: student for i, student in enumerate(students)}
print("\nPosition to Student Name Mapping:")
print(position_to_student)
