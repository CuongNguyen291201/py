for i in range(int(input())):
    s = input()
    s1 = s[::-1]
    flag = "YES"
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s1[i]) - ord(s1[i-1])):
            flag = "NO"
            break
    print(flag)