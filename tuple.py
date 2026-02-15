# ALL TUPLE OPERATIONS IN PYTHON

# 1. TUPLE CREATION
tuple1 = (10, 20, 30, 40)
tuple2 = ("Python", "Java", "C++")

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

# 2. ACCESSING ELEMENTS
print("\nFirst element:", tuple1[0])
print("Last element:", tuple1[-1])

# 3. SLICING
print("Slice (1:3):", tuple1[1:3])

# 4. IMMUTABILITY  
print("\nTuples are immutable (cannot change values)")

# 5. TUPLE OPERATIONS
print("\nLength:", len(tuple1))
print("Max:", max(tuple1))
print("Min:", min(tuple1))
print("Sum:", sum(tuple1))

# 6. CONCATENATION
new_tuple = tuple1 + (50, 60)
print("\nAfter concatenation:", new_tuple)

# 7. REPETITION
print("Repetition:", tuple1 * 2)

# 8. MEMBERSHIP
print("\n20 in tuple1:", 20 in tuple1)
print("100 not in tuple1:", 100 not in tuple1)

# 9. LOOPING THROUGH TUPLE
print("\nLooping through tuple:")
for item in tuple1:
    print(item, end=" ")

# 10. COUNT & INDEX METHODS
tuple3 = (1, 2, 3, 2, 4, 2)
print("\n\nCount of 2:", tuple3.count(2))
print("Index of 3:", tuple3.index(3))

# 11. TUPLE UNPACKING
a, b, c, d = tuple1
print("\nUnpacked values:", a, b, c, d)

# 12. NESTED TUPLE
nested = (1, (2, 3), 4)
print("\nNested tuple:", nested)
print("Access nested value:", nested[1][0])