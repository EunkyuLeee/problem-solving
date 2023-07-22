N = int(input())
M = int(input())
S = input()
count = 0
sList = []

for i in range(M):
    if i < 2:
        sList.append(0)
    elif S[i] == S[i - 2] == 'I' and S[i - 1] == 'O':
        sList.append(sList[i - 2] + 1)
    else:
        sList.append(0)
for i in sList:
    if i >= N:
        count += 1
print(count)
