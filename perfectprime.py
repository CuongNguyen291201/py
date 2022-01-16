import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return x > 1

for i in range(int(input())):
    n = input()
    sum = 0
    flag = True
    for i in n:
        if isPrime(int(i)) == False: 
            flag = False
            break
        sum += int(i)

    if flag and isPrime(int(n)) and isPrime(int(n[::-1])) and isPrime(sum):
        print("Yes")
    else: print("No")