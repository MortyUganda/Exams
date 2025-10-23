from math import *

a, b, c = float(input()), float(input()), float(input())
D = (b ** 2) - (4 * a * c)
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    if x2 > x1:
        print(x1, x2, sep="\n")
    else:
        print(x2, x1, sep="\n")
elif D == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    print("Else some more")
