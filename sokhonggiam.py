for i in range(int(input())):
    s = input()
    b = True
    for j in range(len(s)-1):
        if int(s[j]) > int(s[j+1]):
            b = False
            print("NO")
            break
    if b: print("YES")