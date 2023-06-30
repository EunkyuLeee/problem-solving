n = int(input())
card = []

for i in range(n):
    card.append(i + 1)

i = 0

while i < len(card) - 1:
    card[i] = 0
    i += 1
    card.append(card[i])
    card[i] = 0
    i += 1

print(card[i])
