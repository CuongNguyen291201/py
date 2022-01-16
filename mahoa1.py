for i in range(int(input())):
    s = input()
    d = {}
    for i in s:
        if i not in d: d[i] = 1
        else: d[i] += 1
    for i in d:
        print(str(d[i])+i, end='')
    print()