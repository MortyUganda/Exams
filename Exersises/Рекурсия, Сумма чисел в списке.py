def sum_to(n):
    if len(n) == 0:
        return 0
    else:
        return n[len(n)-1] + sum_to(n[:len(n)-1])
    
print(sum_to([4,5,4,7,10,5,5]))