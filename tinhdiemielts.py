import math

def roundPoint(n):
    natural = math.floor(n)
    decimal = n - natural 
    roundDecimal = 0
    if decimal >= 0 and decimal < 0.25: roundDecimal = 0.0
    elif decimal >= 0.25 and decimal < 0.75: roundDecimal = 0.5
    else: roundDecimal = 1.0
    return natural + roundDecimal

for i in range(int(input())):
    d = {
        '2.5': [3, 4],
        '3.0': [5, 6],
        '3.5': [7, 8, 9],
        '4.0': [10, 11, 12],
        '4.5': [13, 14, 15],
        '5.0': [16, 17, 18, 19],
        '5.5': [20, 21, 22],
        '6.0': [23, 24, 25, 26],
        '6.5': [27, 28, 29],
        '7.0': [30, 31, 32],
        '7.5': [33, 34],
        '8.0': [35, 36],
        '8.5': [37, 38],
        '9.0': [39, 40]
    }

    a = list(str(i) for i in input().split());
    listen, reading = 0,0
    for key, values in d.items():
        for value in values:
            if value == int(a[0]): listen = float(key)
            if value == int(a[1]): reading = float(key)
    print(roundPoint((listen + reading + float(a[2]) + float(a[3]))/4))