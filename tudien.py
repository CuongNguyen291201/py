d = {}
a = []
for i in range(int(input())):
    s = input().split()
    a += s
l = len(a)

a.sort()
for i in a:
    if i not in d: d[i] = 1
    else: d[i] +=1 
sort_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
for k, v in sort_d.items():
    print(f'{k} {v/l}')