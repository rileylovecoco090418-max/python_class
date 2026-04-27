import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/2021_jr_1.txt'
print(file_path)

# Read
f = open(file_path, 'r')
# content = f.read()
# print(type(content))
# print(content)

lines = f.readlines()
# print(type(lines))

b = lines[0]
b = int(b)

p = 5 * b - 400
print(p)
if p > 100:
    print(-1)
elif p < 100:
    print(1)
else:
    print(0)