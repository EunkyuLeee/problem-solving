import sys

n = int(input())
score = 0
c_score = 0
i = 0
j = 0
while i < n:
    a = sys.stdin.readline()
    j = 0
    while j < len(a):
        if a[j] == 'O':
            c_score += 1
            score += c_score
        elif a[j] == 'X':
            c_score = 0
        j += 1
    print(score)
    i += 1
    score = 0
    c_score = 0
