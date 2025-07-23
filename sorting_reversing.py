employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales")
]

sorted_by_salary_asc = sorted(employees, key=lambda x: x[1])
sorted_by_salary_desc = sorted(employees, key=lambda x: x[1], reverse=True)

print("Sorted by Salary (Ascending):")
print(sorted_by_salary_asc)

print("\nSorted by Salary (Descending):")
print(sorted_by_salary_desc)

sorted_by_dept_salary = sorted(employees, key=lambda x: (x[2], x[1]))

print("\nSorted by Department, then by Salary:")
print(sorted_by_dept_salary)

reversed_list = list(reversed(employees))

print("\nReversed List (Original Unchanged):")
print(reversed_list)

sorted_by_name_length = sorted(employees, key=lambda x: len(x[0]))

print("\nSorted by Name Length:")
print(sorted_by_name_length)

sorted_by_name = sorted(employees, key=lambda x: x[0])
print("\nSorted by Name using sorted():")
print(sorted_by_name)

employees_copy = employees[:]
employees_copy.sort(key=lambda x: x[0])
print("\nSorted by Name using .sort():")
print(employees_copy)

print("\nOriginal List Remains Unchanged:")
print(employees)
