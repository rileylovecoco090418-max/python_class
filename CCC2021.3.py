########### Read file block
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/2021_jr_3.txt'
print(file_path)

# Read
f = open(file_path, 'r')
lines = f.readlines()
# print(lines)
lines = [line.strip() for line in lines]
# print(lines)
########### Read file block

########### Logic block
def secret_instructions(instructions):
    prev_dir = None

    for instruct in instructions:
        if instruct == "99999":
            break
        a = int(instruct[0])
        b = int(instruct[1])
        steps = int(instruct[2:])  
        sm = a + b
        if sm == 0:
            direction = prev_dir
        elif sm % 2 == 0:
            direction = "right"
        else:
            direction = "left"
        print(direction, steps)
        prev_dir = direction
########### Logic block

########### Run block
secret_instructions(lines)
########### Run block