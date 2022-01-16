for i in range(int(input())):
    s = input().split('.')
    res = True
    for i in s:
        if i.isnumeric() == False or int(i) > 255 or int(i) < 0:
            res = False
            break
    if res and len(s) == 4: print('YES')


    else: print('NO')
