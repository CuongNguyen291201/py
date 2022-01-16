for i in range(int(input())):
    n = int(input())
    a = list(int(i) for i in input().split())
    c = 0
    res = 0
    while c < 3:
        for i in range(len(a)):
            if a[i] == min(a):

                res+=min(a)
                del a[i]
                c += 1
                break
    print(res)