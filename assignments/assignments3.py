#1.1
dislikes = ["insect", "spider", "cold", "eggplant", "milk"]
print(dislikes)

# 1.2
for item in dislikes:
    print(item)

# 1.3 
print(dislikes[0])

# 1.4
print(dislikes[-1])

# 1.5
print(dislikes[1:])



# 2.1 
thisdict = {"height": 180, "weight": 75, "power": 90, "level": 5}

# 2.2 
print(thisdict.keys())

# 2.3 
print(thisdict.values())

# 2.4 
for key, value in thisdict.items():
    print(key, ":", value)

# 2.5 
thisdict["colour"] = "red"

# Print
print(thisdict)