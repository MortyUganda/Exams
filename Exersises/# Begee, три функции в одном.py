def is_palindrome(psw):
    if len(psw) > 3:
        return False
    return psw[0] == psw[0][::-1]

def is_prime(psw):
    for i in range(2, int(psw[1])):
        if int(psw[1]) % i == 0:
            return False
    return True

def is_valid_password(psw):
    return int(psw[2]) % 2 == 0
# считываем данные
psw = input().split(":")

# вызываем функцию
print(is_valid_password(psw) and is_prime(psw) and is_palindrome(psw))
