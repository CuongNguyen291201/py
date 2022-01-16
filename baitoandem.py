n = int(input())
a = []
while len(a) < n:
    for i in input().split():
        a.append(int(i))
a.sort()
t = 0
for i in range(1, a[-1] + 1):
    if i not in a:
        t += 1
        print(i)
if t == 0: print("Excellent!")