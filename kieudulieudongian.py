for i in range(int(input())):
    a, b = map(int, input().split())
    r1, r2 = 0, 0
    for i in range(1, a):
        if a%i==0: r1+=i
    for i in range(1, b):
        if b%i==0: r2+=i
    print(r1, r2)