for i in range(int(input())):
    s = input()
    res = "YES"
    for i in range(0, len(s)-2):
        if (s[i] != s[i+2]): 
            res = "NO"
            break
    print(res)