import sys

n = int(input())
stack = [0 for i in range(n+1)]
output = []
last = 0
num = 1
isPossible = 1
for i in range(n):
    a = int(sys.stdin.readline())
    for j in range(a - num + 1):
        stack[last] = num
        last += 1
        num += 1
        output.append('+')
    if stack[last-1] != a:
        print('NO')
        isPossible = 0
        break
    output.append('-')
    stack[last] = 0
    last -= 1

if isPossible == 1:
    for i in output:
        print(i)
