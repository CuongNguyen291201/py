for i in range(int(input())):
    n = int(input())
    arr = list(int(i) for i in input().split())
    d = {}
    for i in arr:
        if i not in d: d[i] = 1
        else: d[i] += 1
    b = True
    for i in d:
        if d[i] >= n//2 + 1: 
            b = False
            print(i)
            break
    if b == True: print("NO")