import re
for i in range(int(input())):
    s = input()
    res = re.findall(r"\d+", s)
    m = int(res[0])
    for i in res:
        m = max(int(i), m)
    print(m)