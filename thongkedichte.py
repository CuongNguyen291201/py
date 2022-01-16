m, n = map(int, input().split())
a = []

for i in range(m):
    a.append(list(int (i) for i in input().split()))

x = 0
y = 0

for i in range(m):
    for j in range(n):
        if a[i][j] == -1: x, y = i, j

res = 0
if (x == 0 and y == 0) or (x == 0 and y == n) or (x == m and y == 0) or (x == m and y == n): res += 3
elif x == 0 or y == 0 or x == m or y == n: res += 5
else: res += 8

print(res)