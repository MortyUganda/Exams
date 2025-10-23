from math import asin, cos, pi, sqrt, acos, degrees

def compute_len(x_0,y_0,x_1,y_1):    
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)    
    return len_line

def compute_area(a_1, a_2, a_3):    
    p = (a_1 + a_2 + a_3) / 2   
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))    
    return area

def r (a, b, c):
       k = p/2
       return (((k-a) * (k-b) * (k-c))/k)**0.5

def M(x, b, c):
       return 0.5*(2*(c**2+b**2)-x**2)**0.5

x_a = float(input())
y_a = float(input())
x_b = float(input())
y_b = float(input())
x_c = float(input())
y_c = float(input())

# реализовать решение задачи

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

    # вывести результаты    
if a + b <= c or b + c <= a or a +c <= b:
    print("error")
    
else:     
    s = compute_area(a, b,c)    
    p = a + b + c 
    
    radius = r(a,b,c)
    R = (a*b*c)/(4*s)
    M = M(a, b, c) + M(b, a, c) + M(c, a, b)
    print(round(radius, 4), round(R, 4),round(M, 4))