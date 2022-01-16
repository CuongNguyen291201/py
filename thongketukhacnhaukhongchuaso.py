import collections

a = []
for u in range(int(input())):
    s = input()
    for i in s:
        if (not i.isnumeric()) and (not i.isalpha()) and i != ' ':
            s = s.replace(i, ' ')
    s = s.lower()
    a += s.split(' ')
word_count = collections.Counter(a)
word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
for i in word_count:
    i = list(i)
    i[0] = ''.join([j for j in i[0] if not j.isdigit()])
    if i[0] != '':
        print(i[0], i[1])