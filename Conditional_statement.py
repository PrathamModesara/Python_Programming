
# CONDITIONAL STATEMENTS IN PYTHON
num = int(input("Enter a number: "))

# 1. Simple IF
if num > 0:
    print("Simple IF: Number is Positive")

# 2. IF - ELSE
if num % 2 == 0:
    print("IF-ELSE: Number is Even")
else:
    print("IF-ELSE: Number is Odd")

# 3. ELIF (Else-If Ladder)
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# 4. Nested IF
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    
    if age >= 21:
        print("You are also eligible to contest elections.")
else:
    print("You are not eligible to vote.")

# 5. Ternary Operator
a = 10
b = 20
max_value = a if a > b else b
print("\nTernary: Maximum value is", max_value)