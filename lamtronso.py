for i in range(int(input())):
    s = list(int(i) for i in input())
    for i in range(len(s)-1, 0, -1):
        if s[i]>=5 : s[i-1] += 1
        s[i] = 0
    for i in s:
        print(i, end='')
    print()