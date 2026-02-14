# ALL FUNCTIONS IN PYTHON

# 1. SIMPLE FUNCTION
def greet():
    print("Hello, Welcome to Python!")

greet()

# 2. FUNCTION WITH PARAMETERS
def add(a, b):
    print("Addition =", a + b)

add(10, 5)

# 3. FUNCTION WITH RETURN VALUE
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Multiplication =", result)

# 4. DEFAULT PARAMETERS
def greet_user(name="Guest"):
    print("Hello,", name)

greet_user()
greet_user("Pratham")

# 5. KEYWORD ARGUMENTS
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Rahul")

# 6. VARIABLE LENGTH ARGUMENTS (*args)
def total_sum(*numbers):
    print("Sum =", sum(numbers))

total_sum(1, 2, 3, 4)

# 7. VARIABLE KEYWORD ARGUMENTS (**kwargs)
def details(**info):
    for key, value in info.items():
        print(key, ":", value)

details(name="Pratham", age=21, course="MSc Data Science")

# 8. LAMBDA FUNCTION
square = lambda x: x * x
print("Square =", square(6))

# 9. RECURSIVE FUNCTION
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial =", factorial(5))