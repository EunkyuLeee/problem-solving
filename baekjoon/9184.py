import sys

d = {}


def w(a, b, c):
    temp = str(a) + ' ' + str(b) + ' ' + str(c)
    if temp in d:
        return d[temp]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            d[temp] = 1
        elif a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)
        elif a < b < c:
            d[temp] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            d[temp] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return d[temp]


while True:
    data = sys.stdin.readline().split()
    if data[0] == data[1] == data[2] == '-1':
        break
    str_data = str(data[0]) + ' ' + str(data[1]) + ' ' + str(data[2])
    if str_data in d:
        print("w(%d, %d, %d) = %d" % (int(data[0]), int(data[1]), int(data[2]), d[str_data]))
    else:
        d[str_data] = w(int(data[0]), int(data[1]), int(data[2]))
        print("w(%d, %d, %d) = %d" % (int(data[0]), int(data[1]), int(data[2]), d[str_data]))
