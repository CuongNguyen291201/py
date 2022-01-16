n = int(input())
a = []
d = {}

while len(a) < n:
    a.append(input())

for i in a:
    if i not in d: d[i] = 1
    else: d[i] += 1

print(len(d))