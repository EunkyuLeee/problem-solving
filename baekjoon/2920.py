a = [1, 2, 3, 4, 5, 6, 7, 8]
b = sorted(a, reverse=True)
n = list(map(int, input().split()))
if n == a:
    print("ascending")
elif n == b:
    print("descending")
else:
    print("mixed")
