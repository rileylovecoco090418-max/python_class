import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/2023_jr_1.txt'
print(file_path)

# Read
f = open(file_path, 'r')
# content = f.read()
# print(type(content))
# print(content)

lines = f.readlines()
# print(type(lines))
# print(lines)

P = int(lines[0])
C = int(lines[1])
score = P * 50 - C * 10
if P > C:
    score += 500
print(score)


f.close()