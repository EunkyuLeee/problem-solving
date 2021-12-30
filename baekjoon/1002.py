import sys

t = int(input())
for i in range(t):
    a = list(map(int, sys.stdin.readline().split()))
    if a[2] == a[5]:
        # 거리가 같음
        if a[0] == a[3] and a[1] == a[4]:
            # 위치가 같아 무한대
            print(-1)
        elif (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) > a[2] + a[5]:
            # 둘이 측정한 거리를 합쳐도 둘 사이의 거리가 안됨
            print(0)
        elif (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) == a[2] + a[5]:
            print(1)
        else:
            print(2)
    else:
        # 거리가 다름
        if a[0] == a[3] and a[1] == a[4]:
            # 위치가 같음
            print(0)
        elif (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) > a[2] + a[5]:
            print(0)
        elif (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) == a[2] + a[5]:
            print(1)
        elif (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) + a[2] == a[5] or (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) + a[5] == a[2]:
            # 둘 사이의 거리 + 둘 중 하나가 측정한 거리가 다른 사람이 측정한 거리 (한 원이 다른 원 안에 위치)
            print(1)
        elif (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) + a[2] < a[5] or (abs(a[0] - a[3]) ** 2 + abs(a[1] - a[4]) ** 2) ** (1 / 2) + a[5] < a[2]:
            print(0)
        else:
            print(2)
