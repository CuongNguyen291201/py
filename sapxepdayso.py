for i in range(int(input())):
    n, m = map(int, input().split())
    a = list(int(i) for i in input().split())
    a1, a2 = [], []
    for i in range(len(a)):
        if a[i] == max(a):
            a1 = a[0:i]
            a2 = a[i:len(a)]
    a1.append(m)
    am, duong = [], []
    for j in a1+a2:
        if j < 0: am.append(j)
        else: duong.append(j)
    for j in am+duong: print(j, end=' ')
    print()
