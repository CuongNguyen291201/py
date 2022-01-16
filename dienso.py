for i in range(int(input())):
    n = int(input())
    a = list(int(i) for i in input().split())
    a.sort()
    c = 0
    for i in range(a[0], a[-1]):
        if i not in a: c+=1
    print(c)