a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b:
    min_a_b = a
else:
    min_a_b = b
if b < c:
    min_b_c = b
else:
    min_b_c = c  
if min_a_b < min_b_c:
    print(min_a_b)
else:
    print(min_b_c)