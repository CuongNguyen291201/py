import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return x > 1

for i in range(int(input())):
    s = input()
    c = 0
    for i in s:
        if isPrime(int(i)): 
            c += 1
    if len(s) >= 3 and len(s) <= 500 and isPrime(len(s)) and c > len(s) // 2: 
        print("YES")
    else: print("NO")