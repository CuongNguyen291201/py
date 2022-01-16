import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        if isPrime(i) and str(i) != str(i)[::-1] and isPrime(int(str(i)[::-1])) and int(str(i)[::-1]) <= n:
            if str(i) not in arr and str(i)[::-1] not in arr:
                arr.append(str(i))
                arr.append(str(i)[::-1])
    for i in arr:
        print(i, end=' ')
    print()
