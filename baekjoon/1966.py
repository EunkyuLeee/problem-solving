t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    files = list(map(int, input().split()))
    count = 1
    while m != 0 or max(files) != files[m]:
        if m == 0:
            files.append(files.pop(m))
            m += n - 1
        else:
            if files[0] == max(files):
                n -= 1
                m -= 1
                files.pop(0)
                count += 1
            else:
                files.append(files.pop(0))
                m -= 1
    print(count)
