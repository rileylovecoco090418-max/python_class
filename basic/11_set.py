thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset.add("mango")
print(thisset)

thisset.add("mango")
print(thisset)

thisset.update(("peach,","mango"))
print(thisset)

if "peach" in thisset:
    print("yes")

if "berry" in thisset:
    print("yes")
else:
    print("no")

for item in thisset:
    print(item)

thisset.discard("banana")
print(thisset)

thisset.discard("banana")
print(thisset)

# thisset.remove("berry")
# print(thisset)

thisset.pop()
print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "a"}

print(set1.union(set2))
print(set2.union(set1))
print(set1 | set2)

print(set1.intersection(set2))
print(set2.intersection(set1))
print(set1 & set2)

print(set1.difference(set2))
print(set2.difference(set1))
print(set1 - set2)
print(set2 - set1)

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1 ^ set2)

print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))

set3 = {1, 2, 3}
set4 = {1}
set5 = {4}

print(set3.isdisjoint(set5))
print(set4.isdisjoint(set5))

print(set4.issubset(set3))
print(set4 <= set3)

print(set3.issuperset(set4))
print(set3 >= set4)


