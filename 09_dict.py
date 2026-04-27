# 09_dict.py
"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:
"""

# 1. Create
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964, # this will be overwrited.
  "year": 2020
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))


# 2. Access items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

# 2.1. Get Keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x) #before the change
thisdict["color"] = "white"
print(x) #after the change

# 2.2. Get Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x) #before the change
thisdict["year"] = 2020
print(x) #after the change

# 2.3. Get Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x) #before the change
thisdict["color"] = "red"
print(x) #after the change

# 2.4. Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# 3. Change/Add Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
thisdict.update({"year": 2020})
print(thisdict)


# 4. Remove Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


# 5. Loop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.keys():
  print(x)

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)
 