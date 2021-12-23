n = int(input())

a = list(map(int, input().split()))
# find max value
Max = 0
for i in a:
    if Max < i:
        Max = i
# get new avg
Sum = 0
for i in a:
    Sum += i / Max * 100
print(Sum / n)