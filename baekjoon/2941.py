word = str(input())
c_alphabet = 0
i = 0
while i < len(word):
    if word[i] == 'c' and i < len(word) - 1:
        if word[i+1] == '=' or word[i+1] == '-':
            c_alphabet += 1
            i += 2
        else:
            i += 1
    elif word[i] == 'd' and i < len(word) - 1:
        if word[i+1] == '-':
            c_alphabet += 1
            i += 2
        elif word[i+1] == 'z' and i < len(word) - 2:
            if word[i+2] == '=':
                c_alphabet += 2
                i += 3
            else:
                i += 1
        else:
            i += 1
    elif word[i] == 'l' and i < len(word) - 1:
        if word[i+1] == 'j':
            c_alphabet += 1
            i += 2
        else:
            i += 1
    elif word[i] == 'n' and i < len(word) - 1:
        if word[i+1] == 'j':
            c_alphabet += 1
            i += 2
        else:
            i += 1
    elif word[i] == 's' and i < len(word) - 1:
        if word[i+1] == '=':
            c_alphabet += 1
            i += 2
        else:
            i += 1
    elif word[i] == 'z' and i < len(word) - 1:
        if word[i+1] == '=':
            c_alphabet += 1
            i += 2
        else:
            i += 1
    else:
        i += 1
print(len(word) - c_alphabet)
