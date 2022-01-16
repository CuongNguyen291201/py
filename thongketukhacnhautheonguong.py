import collections

t, k = map(int, input().split())

a = []
for u in range(t):
    s = input()
    for i in s:
        if (not i.isnumeric()) and (not i.isalpha()) and i != ' ':
            s = s.replace(i, ' ')
    s = s.lower()
    a += s.split(' ')
word_count = collections.Counter(a)
word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
for i in word_count:
    if i[0] != '' and i[1] >= k:
        print(i[0], i[1])