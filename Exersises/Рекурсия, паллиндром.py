def is_palindrome(string: str) -> bool:
    k = 0
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    k += 1
    return is_palindrome(string[k: len(string) -1])

print(is_palindrome('1234455544321'))