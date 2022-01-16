n = int(input())
arr = list(int(i) for i in input().split())
count = 0
for i in range(len(arr)-1):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]: count+=1
print(count)