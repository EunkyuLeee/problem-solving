a = [-1 for i in range(26)]
s = input()
for j in range(len(s)):
    if a[ord(s[j]) - 97] == -1:
        a[ord(s[j]) - 97] = j
for k in a:
    print(k, end=' ')
