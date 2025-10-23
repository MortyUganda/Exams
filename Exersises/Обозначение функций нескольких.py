from math import sin
n = int(input())
txt = input()

def square(x):
    return x**2

def coob(x):
    return x**x

def sqrt(x):
    return x**0.5

def modul(x):
    return abs(x)

def sinus(x):
    return sin(x)

func = {'квадрат' : square , 'куб': coob , 'корень': sqrt, 'модуль': modul, 'синус': sinus}

print(func[input()]())
