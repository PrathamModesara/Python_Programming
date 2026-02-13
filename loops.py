# ALL LOOPS IN PYTHON

# 1. FOR LOOP
print("===== FOR LOOP =====")
for i in range(1, 6):
    print(i, end=" ")

# 2. WHILE LOOP
print("\n\n===== WHILE LOOP =====")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1

# 3. DO-WHILE STYLE LOOP
print("\n\n===== DO-WHILE STYLE LOOP =====")
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 5:
        break

# 4. NESTED LOOP (Pattern)
print("\n\n===== NESTED LOOP (Pattern) =====")
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()