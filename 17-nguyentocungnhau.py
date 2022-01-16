def gcd(a, b):
    while a>0:
        if a<b: a, b = b, a
        a = int(a%b)
    return b

n = int(input())
a = list(int(i) for i in input().split())
a.sort()

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if gcd(a[i], a[j])==1: 
            print(int(a[i]), int(a[j]), end=" ")
            print()
