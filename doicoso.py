def convert(n, b):
    res = ""
    tmp = n
    while tmp > 0:
        du = tmp%b
        if du >= 10: res += str(chr(du++55))
        else: res += str(du)
        tmp = int(tmp / b)
    print("".join(reversed(res)))


for i in range(int(input())):
    n, b= map(int, input().split())
    convert(n, b)