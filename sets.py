# ALL SET OPERATIONS IN PYTHON

# 1. SET CREATION
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set1:", set1)
print("Set2:", set2)

# 2. ADDING ELEMENTS
set1.add(50)
print("\nAfter add:", set1)

# 3. UPDATING SET
set1.update([60, 70])
print("After update:", set1)

# 4. REMOVING ELEMENTS
set1.remove(20)     # Error if not present
print("\nAfter remove:", set1)

set1.discard(100)   # No error if not present
print("After discard:", set1)

popped = set1.pop()  # Removes random element
print("Popped element:", popped)
print("After pop:", set1)

# 5. SET OPERATIONS
print("\nUnion:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 6. OPERATORS VERSION
print("\nUnion using | :", set1 | set2)
print("Intersection using & :", set1 & set2)
print("Difference using - :", set1 - set2)
print("Symmetric Difference using ^ :", set1 ^ set2)

# 7. MEMBERSHIP
print("\n30 in set1:", 30 in set1)
print("100 not in set1:", 100 not in set1)

# 8. LOOPING THROUGH SET
print("\nLooping through set1:")
for item in set1:
    print(item, end=" ")

# 9. SET METHODS
print("\n\nIs set1 subset of set2:", set1.issubset(set2))
print("Is set1 superset of set2:", set1.issuperset(set2))
print("Are sets disjoint:", set1.isdisjoint(set2))

# 10. FROZENSET (IMMUTABLE SET)
fset = frozenset([1, 2, 3])
print("\nFrozen set:", fset)