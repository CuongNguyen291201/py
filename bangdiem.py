class BangDiem():
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem
    def result(self):
        ma = self.ma
        ten = self.ten
        diem = self.diem
        hang = ''
        if diem >= 9: hang = 'XUAT SAC'
        elif 8 <= diem <= 8.9: hang = 'GIOI'
        elif 7 <= diem <= 7.9: hang = 'KHA'
        elif 5 <= diem <= 6.9: hang = 'TB'
        else: hang = 'YEU'
        return f'{ma} {ten} {diem} {hang}'  

d = {}

for i in range(int(input())):
    s = input()
    a = list(float(i) for i in input().split())
    ma = ''
    if i < 10: ma = f'HS0{i}'
    else: ma = f'HS{i}'
    sum = 0
    for j in range(len(a)):
        if j == 0 or j == 1: sum += 2*a[j]
        else: sum += a[j]
    diem = float('%.2f' % (sum/12))
    b = BangDiem(ma, s, diem)
    d[f'{i}'] = [diem, b.result()]

sort_d = {k: v for k, v in sorted(d.items(), reverse=True)}
for k, v in d.items():
    print(v[1])
