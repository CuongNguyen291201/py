class NhanVien():
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem

    def result(self):
        ma = self.ma
        ten = self.ten
        diem = self.diem
        loai = ''
        if diem < 5: loai='TRUOT'
        elif 5 <= diem < 8: loai='CAN NHAC'
        elif 8 <= diem <= 9.5: loai = 'DAT'
        else: loai = 'XUAT SAC'
        return f'{ma} {ten} {diem:.2f} {loai}'
d = {}
for i in range(int(input())):
    ten = input()
    ma = ''
    if i < 10: ma = f'TS0{i+1}'
    else: ma = f'TS{i+1}'
    diem1 = float(input())
    diem2 = float(input())
    diem = 0
    if diem1+diem2 > 10: diem = ((diem1 + diem2)/2)/10
    else: diem = (diem1 + diem2)/2

    res = float('%.2f' % diem)
    n = NhanVien(ma, ten, res)
    d[diem] = n.result()
print(d)
sort_d = {k: v for k, v in sorted(d.items(), reverse=True)}
for k, v in sort_d.items():
    print(v)
