def check(n):
    return int(n[::-1])
def check2(n):
    return n%7==0

for i in range(int(input())):
    n = input()
    a = int(n)
    c = 1000
    while c != 0:
        if check2(a) == False:
            a += check(str(a))
            c -= 1
        if check2(a) == True: 
            print(a)
            break
    if c == 0: print(-1)