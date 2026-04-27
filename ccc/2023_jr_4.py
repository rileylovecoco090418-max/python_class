import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = cur_dir + '/2023_jr_4.txt'
f = open(file_path, 'r')
input = f.readline


C = int(input())

top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

answer = 0
for i in range(C):
    if top[i] == 1:
        answer += 3
    if bottom[i] == 1:
        answer += 3

for i in range(C):
    if i > 0 and top[i] == 1 and top[i - 1] == 1:
        answer -= 2
    if i > 0 and bottom[i] == 1 and bottom[i - 1] == 1:
        answer -= 2
    if i % 2 == 0 and top[i] == 1 and bottom[i] == 1:
        answer -= 2

print(answer)
