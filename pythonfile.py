tt = 'abcdefghijklmnopqrstuvxywz_'
s = input().split('.');

if s[len(s)-1] == 'py':
    res = "yes"
    for i in range(len(s)-1):
        if s[i].lower() not in tt:
            res = "no"
            break
    print(res)
else: print("no")