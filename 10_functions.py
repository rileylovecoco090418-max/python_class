"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters(arguments), into a function.

A function can return data as a result.

def function_name(argument1, argument2, ...):
  function body - more code here
"""

# 1. Basic function
def my_function():
  print("Hello from a function")

my_function()

# 2. Function with arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Riley")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
my_function(lname="Refsnes", fname="Emil")

# 3. Default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# 4. Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# 5. Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
