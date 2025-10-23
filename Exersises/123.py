import string
import itertools

def alnum_sequence():
    letters = string.ascii_uppercase
    numbers = range(1,25)
    lst = (el for k in zip(numbers, letters) for el in k)
    return lst

print(*alnum_sequence())