def comparator(char):
    if char.isalpha():
        return 0, char.isupper(), char
    digit = int(char)
    return 1, digit % 2 == 0, digit

string = input()

print(''.join(sorted(string, key=comparator)))