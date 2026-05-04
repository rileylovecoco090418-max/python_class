# 08_tuple.py
"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""

# 1. Create
thistuple = ("apple", "banana", "banana", "cherry")
# thistuple = tuple(("apple", "banana", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(thistuple[0])
print(len(thistuple))
print(type(thistuple))


# 2. Access items
thistuple = ("apple", "banana", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:4])
print(thistuple[:3])
print(thistuple[1:])

# 3. Change/Add
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
# x.append("orange") # This will raise an error

print(x)


# 4. Unpacking a Tuple
# 4.1.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# 4.2. Using Asterisk(*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# 5. Loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# 6. Join Tuples
# 6.1. Join Two Tuples: To join two or more tuples you can use the + operator.
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# 6.2. Multiply Tuples: If you want to multiply the content of a tuple a given number of times, you can use the * operator.
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# print(fruits.count("banana"))
# print(fruits.index("banana"))
