import math

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i==0:
            return False
    return True

for i in range(int(input())):
    c = 0
    s = input()
    for i in s:
        if isPrime(int(i)): c += 1
    if c > int(len(s) / 2): print("YES")
    else: print("NO")