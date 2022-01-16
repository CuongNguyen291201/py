dict = {
    '5': 10000,
    '7': 15000,
    '2': 20000,
    '29': 50000,
    '45': 70000
}

d = {

}

res = 0
for i in range(int(input())):
    s = input().split()
    if len(s) == 5:
        if s[3] == 'IN':
            res += dict[f'{s[2]}']
            d[f'{s[4]}'] = res
print(res)
