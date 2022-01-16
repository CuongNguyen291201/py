d = {}
for i in range(int(input())):
    s = input().split()
    for i in s:
        if i not in d: d[i] = 1
        else: d[i] += 1
sort_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
max = 0
second = 0
for k, v in sort_d.items():
    max = v
    break
for k, v in sort_d.items():
    if v < max: 
        second = v
        break
for k, v in sort_d.items():
    if v == second: 
        print(k, end=' ')