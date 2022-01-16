import math

def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0: return False
    return True

n,m = map(int, input().split())
res = []

for i in range(n):
    a = []
    for j in input().split():
        if isPrime(int(j)): a.append(1)
        else: a.append(0)
    res.append(a)

for i in range(n):
    for j in range(m):
        print(res[i][j], end=" ")
    print()