import sys

N = int(input())
s = []
for i in range(N):
    s.append(int(sys.stdin.readline().strip()))
p = [0 for i in range(N)]
if N < 3:
    print(sum(s))
    exit()
p[N - 1] = s[N - 1]
p[N - 2] = s[N - 1] + s[N - 2]
p[N - 3] = p[N - 1] + s[N - 3]
i = 4
while i <= N:
    idx = N - i
    p[idx] = max(p[idx + 3] + s[idx + 1], p[idx + 2]) + s[idx]
    i += 1

print(max(p[0], p[1]))
