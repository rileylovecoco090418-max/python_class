# 02_variables.py
"""
Variables are placeholder of information
1. Loosely typed
2. Types
3. Single or double quotes?
4. Case-Sensitive
5. Names
6. Assign multiple variables / Unpack a Collection
"""

# 1. Loosely typed
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# 2. Types - Primitive type
x = str(3)    # x will be '3'
y = int(3.2)    # y will be 3
z = float(3.2)  # z will be 3.2
print(x, y, z)

x = 5
y = "John"
# print("Type x: " + type(x))  # error
print("Type x: " + str(type(x)))
print(f"Type y: {type(y)}")

# 3. Single or Double Quotes?
x = "John"
# is the same as
x = 'John'
print(x)
x = 'John is "name"'
print(x)
x = "John is 'name'" + '" abc "'
print(x)

# 4. Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a
print(a, A)

# 5. Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#  Errors
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Camel Case - myVariableName
# Pascal Case - MyVariableName
# Snake Case - my_variable_name

# 6. Assign multiple variables / Unpack a Collection
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# x, y = fruits # Error: too many values to unpack (expected 2)
print(x)
print(y)
print(z)





