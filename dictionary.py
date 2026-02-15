# ALL DICTIONARY OPERATIONS IN PYTHON

# 1. DICTIONARY CREATION
dict1 = {
    "name": "Pratham",
    "age": 22,
    "course": "MSc Data Science"
}

print("Dictionary:", dict1)

# 2. ACCESSING VALUES
print("\nName:", dict1["name"])
print("Age using get():", dict1.get("age"))

# 3. ADDING / UPDATING VALUES
dict1["city"] = "Bangalore"   # Add new key
dict1["age"] = 23             # Update existing key
print("\nAfter adding/updating:", dict1)

# 4. REMOVING ELEMENTS
dict1.pop("city")             # Remove specific key
print("\nAfter pop:", dict1)

# popitem removes last inserted item
removed_item = dict1.popitem()
print("Removed item using popitem():", removed_item)
print("After popitem:", dict1)

# 5. DICTIONARY METHODS
dict2 = {"a": 1, "b": 2, "c": 3}

print("\nKeys:", dict2.keys())
print("Values:", dict2.values())
print("Items:", dict2.items())

# 6. LOOPING THROUGH DICTIONARY
print("\nLooping through keys:")
for key in dict2:
    print(key, end=" ")

print("\nLooping through values:")
for value in dict2.values():
    print(value, end=" ")

print("\nLooping through items:")
for key, value in dict2.items():
    print(key, ":", value)

# 7. CHECKING KEY EXISTENCE
print("\n\nIs 'a' in dict2:", "a" in dict2)
print("Is 'z' not in dict2:", "z" not in dict2)

# 8. COPY DICTIONARY
copy_dict = dict2.copy()
print("\nCopied dictionary:", copy_dict)

# 9. NESTED DICTIONARY
students = {
    "student1": {"name": "Amit", "marks": 85},
    "student2": {"name": "Rahul", "marks": 90}
}

print("\nNested dictionary:", students)
print("Access nested value:", students["student1"]["name"])

# 10. DICTIONARY COMPREHENSION
squares = {x: x*x for x in range(1, 6)}
print("\nDictionary comprehension (squares):", squares)