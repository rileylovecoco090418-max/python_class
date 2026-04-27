D = int(input())

while True:
    yobi = int(input())
    if yobi < D:
        D += yobi
    else:
        print(D)
        break