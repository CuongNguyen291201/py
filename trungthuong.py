for i in range(int(input())):
    d = {}
    n = int(input())
    for i in range(n):
        x = int(input())
        if x not in d: d[x] = 1
        else: d[x] += 1
    max = 1
    res = 1e9
    for i in d: 
        if d[i] > max: max = d[i]
    for i in d:
        if d[i] == max: res = min(res, i)
    print(res)