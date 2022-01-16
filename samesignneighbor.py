n = int(input())
a = list(int(i) for i in input().split())
d = {}
c = 0
for i in range(len(a)-1):
    if (a[i] > 0 and a[i+1] > 0) or (a[i] < 0 and a[i+1] < 0): 
        c += 1
        d[i] = [a[i], a[i+1]]
print(c, end=' ')
sort_d = {k: v for k, v in sorted(list(d.items()), reverse=True)}
for k, values in sort_d.items():
    for v in values:
        print(v, end=' ')
    break
