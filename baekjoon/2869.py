a, b, v = input().split()
a = int(a)
b = int(b)
v = int(v)
v -= a
day = v // (a - b) + 1
if v % (a - b) != 0:
    day += 1
print(day)