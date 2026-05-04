N = int(input().strip())

for _ in range(N):
    s = input().strip()
    letters = []
    total = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch.isupper():
            letters.append(ch)
            i += 1
        elif ch.islower():
            i += 1
        else:
            sign = 1
            if ch == '-':
                sign = -1
                i += 1 
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            total += sign * num
    print("".join(letters) + str(total))