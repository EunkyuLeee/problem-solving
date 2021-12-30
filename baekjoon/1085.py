import sys

x, y, w, h = sys.stdin.readline().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)
x_dis = abs(x - w)
y_dis = abs(y - h)
if x_dis > x:
    x_dis = x
if y_dis > y:
    y_dis = y

if x_dis < y_dis:
    print(x_dis)
else:
    print(y_dis)