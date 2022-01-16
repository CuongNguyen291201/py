import math
l, r = map(int, input().split())

for i in range(l, r-1):
    for j in range(i+1, r):
        for t in range(j+1, r+1):
            if math.gcd(i,j) == math.gcd(i, t) == math.gcd(j, t) ==1:
                print(f"({i}, {j}, {t})")