# 06_loops.py
"""
Loops
"""

# For loops: Range
for x in range(6):
    print(x)
    # print(x + 1)

# For loops: List, break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    # print(x)
    if x == "banana":
        break
    print(x)

# For loops: List, continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# While loops
i = 1
while i < 6: # If it is true, run the loop
    print(i)
    i += 1 # i = i + 1

# Nested loop
for x in range(3):
    print(x)
    for y in range(2): # 0, 1
        print(x, y)
