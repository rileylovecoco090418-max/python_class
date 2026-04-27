import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/2023_jr_2.txt'
print(file_path)

# Read
f = open(file_path, 'r')
# content = f.read()
# print(type(content))
# print(content)

lines = f.readlines()
# print(type(lines))
# print(lines)


peppers = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

N = int(lines[0])
total = 0
for i in range(N):
    name = lines[i + 1].strip()
    total += peppers[name]
print(total)