def gcd(a, b):
    while a>0:
        if a<b: a, b = b, a
        a = int(a%b)
    return b

for i in range(int(input())):
    s = input()
    r = s[::-1]

    if gcd(int(s), int(r)) == 1: print("YES")
    else: print("NO")