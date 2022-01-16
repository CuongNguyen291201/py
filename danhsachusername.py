d = {}
for i in range(int(input())):
    s = input().lower()
    if s not in d: d[s] = 1
    else: d[s] += 1
sort_d = {k: v for k, v in sorted(list(d.items()))}
for k, v in sort_d.items():
    print(k)