def digitSum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

number = input()
c = 0
sum = 0
if len(number) > 1:
    for i in number:
        sum += (ord(i)-ord('0'))
    c += 1
    number = sum
    c = 1
    if number >= 10:
        while True:
            c += 1
            number = digitSum(number)
            if number < 10:
                break
print(c)