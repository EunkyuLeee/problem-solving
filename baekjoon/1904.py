n = int(input())
d = {1: 1, 2: 2}
for i in range(1, n-1):
    d[i+2] = (d[i+1] + d[i]) % 15746
print(d[n])
