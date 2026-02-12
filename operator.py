# ALL OPERATORS IN PYTHON
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print("===== ARITHMETIC OPERATORS =====")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)     
print("a // b =", a // b)     

print("\n===== COMPARISON OPERATORS =====")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\n===== LOGICAL OPERATORS =====")
print("a > 5 and b < 10 :", a > 5 and b < 10)
print("a > 5 or b > 10  :", a > 5 or b > 10)
print("not(a > b) :", not(a > b))

print("\n===== ASSIGNMENT OPERATORS =====")
x = 10
print("x =", x)
x += 5
print("x += 5 ->", x)
x -= 3
print("x -= 3 ->", x)
x *= 2
print("x *= 2 ->", x)
x /= 2
print("x /= 2 ->", x)
x %= 3
print("x %= 3 ->", x)
x **= 2
print("x **= 2 ->", x)
x //= 2
print("x //= 2 ->", x)

print("\n===== BITWISE OPERATORS =====")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)

print("\n===== MEMBERSHIP OPERATORS =====")
list1 = [1, 2, 3, 4]
print("2 in list1 :", 2 in list1)
print("5 not in list1 :", 5 not in list1)

print("\n===== IDENTITY OPERATORS =====")
p = [1, 2]
q = p
r = [1, 2]

print("p is q :", p is q)
print("p is r :", p is r)
print("p is not r :", p is not r)

print("\n===== TERNARY OPERATOR =====")
max_value = a if a > b else b
print("Max value =", max_value)