D = int(input().strip())
E = int(input().strip())

for _ in range(E):
    op = input().strip()  
    Q = int(input().strip())
    if op == '+':
        D += Q
    else:
        D -= Q

print(D)