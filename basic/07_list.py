# 07_list.py
"""
List
 - Lists are used to store multiple items in a single variable.
 - List items are ordered, changeable, and allow duplicate values.
 - List items are indexed, the first item has index [0], the second item has index [1] etc.

"""


# 1.Create
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# 2. Length and Type
print(len(thislist))
print(type(thislist))


# 3. Access
print(thislist[1])
print(thislist[-1])
print(thislist[1:4])
print(thislist[:3])
print(thislist[1:])


# Check if item is in the list
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Different data types
list1 = ["abc", 34, True, 40, "male"]


# 4. Change/Add
thislist[1] = "blackcurrant"
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# 5. Remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# 6. Loops
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])


# 7. Sort
thislist = [100, 50, 65, 82, 23]
thislist.sort()
# thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# 8. Copy
thislist = ["apple", "banana", "cherry"]
mylist1 = thislist.copy()
print(mylist1)

mylist2 = list(thislist)
print(mylist2)


# 9. Join
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

