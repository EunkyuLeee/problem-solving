l = int(input())
s = input()
m = 1234567891

t = 0
for i, j in enumerate(s):
    mul = 1
    for k in range(i):
        mul *= 31
        mul %= m
    t += ((ord(j) - ord('a') + 1) * mul)
print(t % m)
