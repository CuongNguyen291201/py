s = input()
res = ''
for i in s:
    if i == ' ': res += i
    if i.islower():
        res += i.upper()
    if i.isupper(): res += i.lower()
print(res)