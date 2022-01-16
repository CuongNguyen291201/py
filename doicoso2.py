def convert(n, b):
    res = ""
    tmp = n
    while tmp > 0:
        du = tmp%b
        if du >= 10: res += str(chr(du++55))
        else: res += str(du)
        tmp = int(tmp / b)
    print("".join(reversed(res)))

def toDecimal(s):
    decimal = 0
    for i in s:
        decimal = decimal * 2 + int(i)
    return decimal

for i in range(int(input())):
    b = int(input())
    s = input()
    t = toDecimal(s)
    convert(t, b)