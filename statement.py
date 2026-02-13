# 5. BREAK STATEMENT
print("\n===== BREAK EXAMPLE =====")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")

# 6. CONTINUE STATEMENT
print("\n\n===== CONTINUE EXAMPLE =====")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")

# 7. PASS STATEMENT
print("\n\n===== PASS EXAMPLE =====")
for i in range(3):
    pass  # does nothing
print("Pass executed successfully.")