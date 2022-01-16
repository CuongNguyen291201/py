for i in range(int(input())):
    n,m = map(int, input().split())
    a = list(str(i) for i in input().split())
    res = a[m:n] + a[0:m]
    for i in res:
        print(i, end=' ')
    print()