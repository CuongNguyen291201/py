for i in range(int(input())):
    n = int(input())
    a = list(int(i) for i in input().split())
    b = list(int(i) for i in input().split())

    a.sort()
    b.sort()
    res = "YES"
    for i in range(n):
        if a[i] > b[i]:
            res = "NO"
            break
    print(res)