# 04_operators.py
### 1. Arithmetic Operators
print(f'Addtion: 10 + 3 = {10 + 3}')
print(f'Substraction: 10 - 3 = {10 - 3}')
print(f'Multiplication: 10 x 3 = {10 * 3}')
print(f'Division: 10 / 3 = {10 / 3}')
print(f'Modulus(Remainder): 10 % 3 = {10 % 3}')
print(f'Exponentiation: 10^3 = 10 x 10 x 10 = {10 ** 3}')
print(f'Floor division: 10 // 3 = {10 // 3}')


### 2. Assignment Operators
x = 10
x += 3 # x = x + 3
print(f'Addtion: 10 + 3 = {x}')
x = 10
x -= 3 # x = x - 3
print(f'Substraction: 10 - 3 = {x}')
x = 10
x *= 3
print(f'Multiplication: 10 x 3 = {x}')
x = 10
x /= 3
print(f'Division: 10 / 3 = {x}')
x = 10
x %= 3
print(f'Modulus(Remainder): 10 % 3 = {x}')
x = 10
x **= 3
print(f'Exponentiation: 10^3 = 10 x 10 x 10 = {x}')
x = 10
x //= 3
print(f'Floor division: 10 // 3 = {x}')


### 3. Comparison Operators
"""
Equal: ==
Not equal: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=
"""

### 4. Logical Operators
# and - Returns True if both statements are true
x = 7
print(x > 5 and x < 10)
print(x < 5 and x > 10)

# or - Returns True if one of the statements is true
x = 7
print(x < 5 or x < 10)
print(x < 5 or x > 10)
10
# and - Reverse the result, returns False if the result is true
x = 7
print(not(x < 5))
print(not(x > 5 and x < 10))

"""
### 5. Etc
 - Identity operators
 - Membership operators
 - Bitwise operators
"""