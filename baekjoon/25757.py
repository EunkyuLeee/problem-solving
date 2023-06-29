n, g = input().split()

nSet = set()
play = {'Y': 2, 'F': 3, 'O': 4}
n = int(n)

for i in range(n):
    name = input()
    nSet.add(name)

print(len(nSet) // (play[g] - 1))
