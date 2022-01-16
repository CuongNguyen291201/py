class TrungTuyen():
    def __init__(self, ma, ten, khoi, diem):
        self.ma = ma
        self.ten = ten
        self.khoi = khoi
        self.diem = diem
    def result(self):
        trungtuyen = ''
        if self.diem >= 18.0: trungtuyen = 'TRUNG TUYEN'
        else: trungtuyen = 'LOAI'
        return f'{self.ma} {self.ten} {self.khoi} {self.diem} {trungtuyen}'
d = {}
ut = {
    '1': 2.0,
    '2': 1.5,
    '3': 1.0,
    '4': 0.0
}
k = {
    'A': 'TOAN',
    'B': 'LY',
    'C': 'HOA'
}
for i in range(int(input())):
    ten = input()
    khoi = input()
    ma = ''
    if i < 10: ma = f'GV0{i+1}'
    else: ma = f'GV{i+1}'
    d1 = float(input()) * 2
    d2 = float(input())
    khoihoc = k[khoi[0]]
    uutien = khoi[1]
    diem = d1+d2+ut[uutien]
    trungtuyen = TrungTuyen(ma, ten, khoihoc, diem)
    d[diem] = trungtuyen.result()

print(d)
sort_d = {k: v for k, v in sorted(list(d.items()))}
for k, v in d.items():
    print(v)