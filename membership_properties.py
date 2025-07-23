fruit_list = ["apple", "banana", "orange", "apple","grape"]
fruit_tuple = ("apple", "banana","orange")
fruit_set = {"apple", "banana", "orange","grape"}
fruit_dict = {"apple": 5, "banana": 3, "orange": 8,"grape": 2}

structures = {
    "List": fruit_list,
    "Set": fruit_set,
    "Tuple": fruit_tuple,
    "Dictionary": fruit_dict
}

print("Membership Check for 'apple':")
for name, structure in structures.items():
    if name == "Dictionary":
        present = "apple" in structure.keys()
    else:
        present = "apple" in structure
    print(f"- {name}: {'✅ Present' if present else '❌ Not Present'}")

print("\nLength of Each Structure:")
for name, structure in structures.items():
    print(f"- {name}: {len(structure)} elements")

print("\nElements in Each Structure:")
for name, structure in structures.items():
    print(f"- {name}:")
    if name == "Dictionary":
        for key, value in structure.items():
            print(f"  {key} → {value}")
    else:
        for item in structure:
            print(f"  {item}")

print("\nMembership Testing Performance:")
print("""
- Sets and Dictionaries offer **O(1)** average time complexity for membership tests because they use hash tables.
- Lists and Tuples require **O(n)** time in the worst case since they search sequentially.
- So, for large datasets, prefer Sets or Dictionaries for fast lookup.
""")
    
print("Iteration Patterns Summary:")
print("""
- List:        for item in fruit_list
- Set:         for item in fruit_set
- Tuple:       for item in fruit_tuple
- Dictionary:  for key, value in fruit_dict.items()
""")
