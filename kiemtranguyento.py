import math

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i==0:
            return False
    return True

for i in range(int(input())):
    s = input()
    a = ''
    for i in range(len(s)-1, len(s)-5, -1): 
        a += s[i]
    if isPrime(int("".join(reversed(a)))): print("YES")
    else: print("NO")