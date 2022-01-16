P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    s = input().split()
    t = int(s[0])
    if t==0: break
    res = ''
    for i in s[1]:
        l = P.find(i)
        res += P[(l+t)%28]
    print(res[::-1])