vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    isHaveV = False
    isAcceptable = True
    pw = input()
    if pw == "end":
        break
    for i, c in enumerate(pw):
        if i < len(pw) - 1 and c == pw[i + 1] and c != 'e' and c != 'o':
            isAcceptable = False
        if c in vowel:
            isHaveV = True
            if i < len(pw) - 2:
                for j in range(1, 3):
                    if not pw[i + j] in vowel:
                        break
                    elif j == 2:
                        isAcceptable = False
        else:
            if i < len(pw) - 2:
                for j in range(1, 3):
                    if pw[i + j] in vowel:
                        break
                    elif j == 2:
                        isAcceptable = False
    if isAcceptable and isHaveV:
        print("<" + pw + "> is acceptable.")
    else:
        print("<" + pw + "> is not acceptable.")
