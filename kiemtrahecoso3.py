arr = ['0', '1', '2']
for i in range(int(input())):
    s = input()
    res = "YES"
    for i in s:
        if str(i) not in arr:
            res="NO"
            break
    print(res)