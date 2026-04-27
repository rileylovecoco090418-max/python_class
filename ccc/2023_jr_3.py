import sys

sys.stdin = open("input.txt", "r")
N = int(input().strip())
days = [0, 0, 0, 0, 0]
for _ in range(N):
    s = input().strip()
    for i in range(5):
        if s[i] == 'Y':
            days[i] += 1
best = max(days)
answer = []
for i in range(5):
    if days[i] == best:
        answer.append(str(i + 1))
print(",".join(answer))