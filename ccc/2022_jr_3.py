s = input().strip()
i = 0

while i < len(s):
    letters = ""
    while i < len(s) and s[i].isalpha():
        letters += s[i]
        i += 1
    sign = s[i] 
    action = "tighten" if sign == '+' else "loosen"
    i += 1
    num = ""
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    print (f"{letters} {actions} {num}")
    print(letters, action, num)