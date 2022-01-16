for i in range(int(input())):
    s = input()
    a = int(s[0] + s[1])
    b = int(s[len(s)-2]+s[len(s)-1])
    if a == b: print("YES")
    else: print("NO")
