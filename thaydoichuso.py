for i in range(int(input())):
    p, q = map(str, input().split())
    a = input()
    b = input()

    if int(q) < int(p): p,q = q,p

    so1a = a.replace(p, q)
    so1b = b.replace(p, q)

    so2a = so1a.replace(q,p)
    so2b = so1b.replace(q,p)

    max = int(so1a) + int(so1b)
    min = int(so2a) + int(so2b)

    print(f'{min} {max}')
    # print(a.replace(p, q))
    # print(b.replace(p, q))


    # min = int(mina) + int(minb)
    # max = int(maxa) + int(maxb)
    # print(mina, minb, maxa, maxb)

    # print(min, max, end=' ')
    # print()