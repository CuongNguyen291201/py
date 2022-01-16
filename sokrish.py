import math

for i in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += math.factorial(int(i))
    if int(s) == sum: print("Yes")
    else: print("No")