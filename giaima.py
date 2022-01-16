for i in range(int(input())):
    s = input()
    a = []
    b = []
    for i in s:
        if i.isdigit(): b.append(int(i))
        else: a.append(i)
    for i in range(len(a)):
        print(a[i]*b[i], end="")
    print()