# ALL EXCEPTION HANDLING IN PYTHON

# 1. BASIC TRY-EXCEPT
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Division =", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

# 2. MULTIPLE EXCEPT BLOCKS
try:
    list1 = [1, 2, 3]
    print(list1[5])
except IndexError:
    print("Error: Index out of range!")

# 3. GENERIC EXCEPTION
try:
    x = int("Python")
except Exception as e:
    print("Generic Error:", e)

# 4. ELSE BLOCK
try:
    num = int(input("\nEnter a positive number: "))
    if num < 0:
        raise ValueError("Negative number not allowed!")
except ValueError as e:
    print("Error:", e)
else:
    print("You entered:", num)

# 5. FINALLY BLOCK
try:
    file = open("sample.txt", "r")
    print("\nFile opened successfully.")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Finally block executed (always runs).")

# 6. CUSTOM EXCEPTION
class AgeError(Exception):
    pass

try:
    age = int(input("\nEnter your age: "))
    if age < 18:
        raise AgeError("You must be 18 or older!")
    print("Access granted.")
except AgeError as e:
    print("Custom Exception:", e)

# 7. ASSERT STATEMENT
try:
    value = int(input("\nEnter a number greater than 10: "))
    assert value > 10, "Value must be greater than 10!"
    print("Valid input.")
except AssertionError as e:
    print("Assertion Error:", e)