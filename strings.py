# ALL STRING OPERATIONS IN PYTHON

# 1. STRING CREATION
str1 = "Hello"
str2 = "World"

print("String 1:", str1)
print("String 2:", str2)

# 2. STRING CONCATENATION
full = str1 + " " + str2
print("\nConcatenation:", full)

# 3. STRING REPETITION
print("Repetition:", str1 * 3)

# 4. STRING LENGTH
print("Length:", len(full))

# 5. INDEXING
print("First character:", full[0])
print("Last character:", full[-1])

# 6. SLICING
print("Slice (0-5):", full[0:5])
print("Reverse string:", full[::-1])

# 7. STRING METHODS
text = "  python programming  "

print("\nUpper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Strip:", text.strip())
print("Replace:", text.replace("python", "Java"))
print("Split:", text.split())

# 8. STRING CHECK METHODS
check = "Python123"

print("\nIs Alpha:", check.isalpha())
print("Is Digit:", check.isdigit())
print("Is Alnum:", check.isalnum())
print("Starts with Py:", check.startswith("Py"))
print("Ends with 3:", check.endswith("3"))

# 9. STRING FORMAT
name = "Pratham"
age = 22

print("\nUsing format(): My name is {} and I am {} years old.".format(name, age))
print(f"Using f-string: My name is {name} and I am {age} years old.")

# 10. MEMBERSHIP OPERATOR
print("\n'Python' in full:", "Python" in full)
print("'Java' not in full:", "Java" not in full)
