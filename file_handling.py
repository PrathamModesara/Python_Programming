# ALL FILE HANDLING IN PYTHON

# 1. WRITE TO FILE (w mode)
file = open("sample.txt", "w")
file.write("Hello, this is Python file handling.\n")
file.write("Welcome to MSc Data Science.\n")
file.close()

print("Data written successfully (w mode).")

# 2. READ FILE (r mode)
file = open("sample.txt", "r")
content = file.read()
print("\nReading full file using read():")
print(content)
file.close()

# 3. APPEND FILE (a mode)
file = open("sample.txt", "a")
file.write("This line is appended.\n")
file.close()

print("Data appended successfully (a mode).")

# 4. READ LINE BY LINE
file = open("sample.txt", "r")
print("\nReading file line by line:")
for line in file:
    print(line.strip())
file.close()

# 5. USING WITH STATEMENT
print("\nUsing 'with' statement:")
with open("sample.txt", "r") as file:
    print(file.readline())   

# 6. FILE MODES
print("\nFile Modes:")
print("r  -> Read")
print("w  -> Write (overwrite)")
print("a  -> Append")
print("r+ -> Read and Write")
print("rb -> Read binary")
print("wb -> Write binary")

# 7. CHECK FILE PROPERTIES
with open("sample.txt", "r") as file:
    print("\nFile Name:", file.name)
    print("File Mode:", file.mode)
    print("Is Closed:", file.closed)

# 8. EXCEPTION HANDLING
try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\nError: File not found!")