class HoaDon(object):
    def __init__(self, ma, ten, tien):
        self.ma = ma
        self.ten = ten
        self.tien = tien
    def result(self):
        return f'{self.ma} {self.ten} {self.tien}'
d = {}
for i in range(int(input())):
    ten = input()
    ma = ''
    if i < 10: ma = f'KH0{i+1}'
    else: ma = f'KH{i+1}'
    a = int(input())
    b = int(input())
    tien = 0
    soluong = abs(a-b)
    if abs(a-b) <= 50: tien = soluong*100*1.02
    elif 51 <= soluong <= 100: tien = soluong*150*1.03
    else: tien = soluong*200*1.05

    d[tien] = HoaDon(ma, ten, int(tien)).result()

sort_d = {k: v for k, v in sorted(d.items(), reverse=True)}
for k, v in d.items():
    print(v)