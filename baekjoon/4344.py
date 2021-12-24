import sys

c = int(input())
for i in range(c):
    a = list(map(int, sys.stdin.readline().split()))
    numOfStudents = a[0]
    del a[0]

    # find avg
    Avg = sum(a) / len(a)

    # find number of upper value than avg
    num = 0
    for j in a:
        if j > Avg:
            num += 1

    print('%0.3f' % float(num / len(a) * 100) + "%")
