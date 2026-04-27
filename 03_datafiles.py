"""
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

What to know for now:
  str, int, float, bool
What to know for next time:
  list, tuple, range, dict, set
What don't need to know in near future:
  complex, frozenset, bytes, bytearray, memoryview
"""

# Check the type
x = 5
print(type(x))

# str
x = "Hello World"
x = str("Hello World")
# int
x = 20
x = int(20)
# float
x = 20.5
x = float(20.5)
# bool
x = True
x = bool(5) # Is it True? or False?
x = bool(0) # Is it True? or False?


# list
x = ["apple", "banana", "cherry"]
x = list(("apple", "banana", "cherry"))
# tuple
x = ("apple", "banana", "cherry")
x = tuple(("apple", "banana", "cherry"))
# range
x = range(6)
# dict
x = {"name" : "John", "age" : 36}
x = dict(name="John", age=36)
# set
x = {"apple", "banana", "cherry"}
x = set(("apple", "banana", "cherry"))


# Type casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
