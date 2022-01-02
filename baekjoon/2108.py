import sys
from collections import Counter

n = int(input())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
Sum = sum(a)
print(round(Sum / n))
print(a[n//2])
temp = Counter(a).most_common()
if len(temp) >= 2:
    if temp[0][1] == temp[1][1]:
        mc = temp[1][0]
    else:
        mc = temp[0][0]
else:
    mc = temp[0][0]
print(mc)
print(max(a) - min(a))
