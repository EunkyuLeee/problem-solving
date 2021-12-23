import sys
index = [0 for i in range(42)]
result = 0
for i in range(10):
    a = int(sys.stdin.readline())
    index[a % 42] += 1
for i in index:
    if i != 0:
        result += 1
print(result)