def fac(a):
    if a == 1 or a == 0:
        return 1
    return fac(a-1) * a


print(fac(int(input())))
