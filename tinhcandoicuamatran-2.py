n = int(input())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
k = int(input())

top, down = 0, 0
t = 0
for i in range(n):
    for j in range(n-1-i):
        top += a[i][j]
for i in range(n):
    for j in range(n-i, n):
        down += a[i][j]

if abs(top - down) <= k:
    print("YES")
else:
    print("NO")
print(abs(top - down))
