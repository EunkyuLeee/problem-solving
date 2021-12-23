a = int(input())
b = int(input())
c = int(input())
index = [0 for i in range(10)]
temp = 1
value = a * b * c
while temp < value:
    temp *= 10
    index[(value % temp) // (temp // 10)] += 1
for i in index:
    print(i)