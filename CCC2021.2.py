n = int(input())

best_name = ""
best_bid = -1

for _ in range(n):
    name = input().strip()
    bid = int(input().strip())
    if bid > best_bid:         
        best_bid = bid
        best_name = name
print(best_name)