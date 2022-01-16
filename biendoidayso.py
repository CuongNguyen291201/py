def allEqual(d):
    return d[0] == d[1] == d[2] == d[3]

while True:
    arr = list(int(i) for i in input().split())
    count = 0;
    if arr[0] == 0 and allEqual(arr) == True: break
    while allEqual(arr) == False:
        tmp = arr[0]
        arr[0] = abs(arr[0]-arr[1]) 
        arr[1] = abs(arr[1]-arr[2]) 
        arr[2] = abs(arr[2]-arr[3]) 
        arr[3] = abs(arr[3]-tmp)
        count += 1
    print(count)