from itertools import combinations

n, m = map(int, input().split())
a = list(int(i) for i in input().split())
b = list(set(a))
comb = combinations(b, m)
for i in list(comb):
    for item in i:
        print(item, end=' ')
    print()