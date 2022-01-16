def gcd(a, b):
    while a>0:
        if a<b: a, b = b, a
        a = int(a%b)
    return b

n = int(input())
arr = list(int(i) for i in input().split())
arr.sort()

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if gcd(arr[i], arr[j]) == 1:
            print(arr[i], arr[j], end=' ')
            print()