def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = int(a % b)
    return b


a, b = map(int, input().split())
t = 0
for i in range(10**(b-1), 10**(b)):
    if gcd(a, i) == 1:
        t += 1
        print(i, end=' ')
    if t == 10:
        t = 0
        print()
