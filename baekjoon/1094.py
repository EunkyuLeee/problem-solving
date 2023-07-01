x = int(input())
m = 1

while m <= x:
    m *= 2
m /= 2
count = 0
while x != 0:
    if x >= m:
        x -= m
        count += 1
    m /= 2

print(count)
