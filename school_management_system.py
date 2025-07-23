school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}

print("Teacher Names:")
for subject, info in school.items():
    teacher = info["teacher"]
    print(f"- {subject}: {teacher}")

print("\nClass Average Grades:")
for subject, info in school.items():
    students = info["students"]
    total = sum(grade for _, grade in students)
    avg = total / len(students)
    print(f"- {subject}: {avg:.2f}")

top_student = ("", 0)
for subject, info in school.items():
    for name, grade in info["students"]:
        if grade > top_student[1]:
            top_student = (name, grade)

print(f"\nTop Student Across All Classes:\n- {top_student[0]} with grade {top_student[1]}")

print("\nStudent Names and Grades by Class:")
for subject, info in school.items():
    print(f"\n{subject}:")
    for name, grade in info["students"]:
        print(f"  - {name}: {grade}")
