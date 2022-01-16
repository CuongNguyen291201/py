n = int(input())
a = []
d = {
    '6': 0,
    '7': 0
}

while len(a) < n:
    a.append(input())


t = 0
for i in range(0, len(a)-4, t):
    if (len(a[i].split()) == 6) and len(a[i+2].split()) != 6:
        d['6'] += 1
        t = 2

    if len(a) >= 4 and len(a[i].split()) == 7 and len(a[i+4].split()) != 7:
        d['7'] += 1
        t = 4
    print(i, a[i])
print(d)