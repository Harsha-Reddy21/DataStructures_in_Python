grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced_grades = grades[2:7]
print("Sliced (index 2 to 6):", sliced_grades)

above_85 = [grade for grade in grades if grade > 85]
print("Grades above 85:", above_85)

grades[3] = 95
print("After replacing index 3 with 95:", grades)

grades.extend([82, 97, 84])
print("After adding 3 new grades:", grades)

sorted_grades = sorted(grades, reverse=True)
top_5 = sorted_grades[:5]
print("Top 5 grades:", top_5)
