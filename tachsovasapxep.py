import re

a = []
b = []

for i in range(int(input())):
    s = input()
    res = re.findall(r"\d+", s)
    a+=res
for i in a: b.append(int(i))
b.sort()
for i in b: print(i)