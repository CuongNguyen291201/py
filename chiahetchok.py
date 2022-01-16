a, k, n = map(int, input().split())
res = []
for i in range(1, int(n/k)+1):
    t = i*k-a
    if t>0: res.append(t)
if len(res) == 0: print(-1)
else: 
    for i in res: print(i, end=' ')
        