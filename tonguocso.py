import math

def check():
    sum = 0
    n = int(input())
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            sum += (i * count)
    if n > 1:
        sum += n
    return sum

res = 0
for i in range(int(input())):
    res += check()
print(res)