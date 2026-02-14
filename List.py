# ALL LIST OPERATIONS IN PYTHON

# 1. LIST CREATION
list1 = [10, 20, 30, 40]
list2 = ["Python", "Java", "C++"]

print("List1:", list1)
print("List2:", list2)

# 2. ACCESSING ELEMENTS
print("\nFirst element:", list1[0])
print("Last element:", list1[-1])

# 3. SLICING
print("Slice (1:3):", list1[1:3])

# 4. MODIFYING ELEMENTS
list1[1] = 25
print("\nAfter modification:", list1)

# 5. ADDING ELEMENTS
list1.append(50)          
list1.insert(1, 15)        
print("\nAfter append & insert:", list1)

# 6. EXTEND LIST
list1.extend([60, 70])
print("After extend:", list1)

# 7. REMOVING ELEMENTS
list1.remove(25)           
popped = list1.pop()      
print("\nAfter remove & pop:", list1)
print("Popped value:", popped)

# 8. LIST OPERATIONS
print("\nLength:", len(list1))
print("Max:", max(list1))
print("Min:", min(list1))
print("Sum:", sum(list1))

# 9. SORTING
list1.sort()
print("\nSorted list:", list1)

list1.sort(reverse=True)
print("Descending order:", list1)

# 10. REVERSE
list1.reverse()
print("Reversed list:", list1)

# 11. MEMBERSHIP
print("\n20 in list1:", 20 in list1)
print("100 not in list1:", 100 not in list1)

# 12. LOOPING THROUGH LIST
print("\nLooping through list:")
for item in list1:
    print(item, end=" ")

# 13. LIST COMPREHENSION
squares = [x*x for x in range(1, 6)]
print("\n\nList comprehension (squares):", squares)

# 14. COPYING LIST
copy_list = list1.copy()
print("\nCopied list:", copy_list)
