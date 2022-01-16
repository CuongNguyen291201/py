import math

n, x = map(int, input().split())

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

arrP = [2]
k = 2
while len(arrP) < n:
    k += 1
    if isPrime(k): arrP.append(k)

for i in range(0, n):
    print(x, end=' ')
    x += arrP[i]
print(x)

