from datetime import datetime

d = {
    'Bach Duong': ['21/03/2000', '19/04/2000'],
    'Kim Nguu': ['20/04/2000', '20/05/2000'],
    'Song Tu': ['21/05/2000', '20/06/2000'],
    'Cu Giai': ['21/06/2000', '22/07/2000'],
    'Su Tu': ['23/07/2000', '22/08/2000'],
    'Xu Nu': ['23/08/2000', '22/09/2000'],
    'Thien Binh': ['23/09/2000', '22/10/2000'],
    'Thien Yet': ['23/10/2000', '22/10/2000'],
    'Nhan Ma': ['23/11/2000', '21/12/2000'],
    'Ma Ket': ['22/12/2000', '19/01/2001'],
    'Bao Binh': ['20/01/2000', '18/02/2000'],
    'Song Ngu': ['19/02/2000', '20/03/2000']
}

for i in range(int(input())):
    a, b = map(str, input().split())
    if len(a) == 1: a = '0'+a
    if len(b) == 1: b = '0'+b
    if b == '01' and int(a) < 20: date = a+'/'+b+'/2001'
    else: date = a+'/'+b+'/2000'
    d1 = datetime.strptime(date, "%d/%m/%Y")
    for key, values in d.items():
        if d1 >= datetime.strptime(values[0], "%d/%m/%Y") and d1 <= datetime.strptime(values[1], "%d/%m/%Y"):
            print(key)
            break