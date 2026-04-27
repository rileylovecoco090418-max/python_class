N = int(input())
count = 0

for _ in range(N):
    points = int(input())
    fouls = int(input())
    rating = points * 5 - fouls * 3
    if rating > 40:
        count += 1

if count == N:
    print(f"{count}+")
else:
    print(count)