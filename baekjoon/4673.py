def isHaveGen(a):
    for n in range(a):
        Sum = n + ((n % 10000) // 1000) + ((n % 1000) // 100) + ((n % 100) // 10) + ((n % 10) // 1)
        if Sum == a:
            return True
    return False


i = 0
while i < 10000:
    i += 1
    if not isHaveGen(i):
        print(i)
