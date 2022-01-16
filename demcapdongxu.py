import math
n = int(input())
row = [0]*n 
col = [0]*n

res = 0
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == 'C':
            row[i] += 1
            col[j] += 1
for i in row:
    if i >= 2: res += math.comb(i, 2)
for i in col:
    if i >= 2: res += math.comb(i, 2)
print(res)