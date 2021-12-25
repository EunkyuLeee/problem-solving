n = int(input())
group = 0
for j in range(n):
    i = 1
    num = [0 for k in range(26)]
    word = str(input())
    num[ord(word[0]) - 97] = 1
    while i < len(word):
        if word[i-1] != word[i]:
            num[ord(word[i])-97] += 1
        i += 1
    if max(num) == 1:
        group += 1
print(group)
