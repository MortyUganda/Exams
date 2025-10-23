n = input()

total = "".join(n.split("-"))
s = "-"

flag = True

for i in range(len(total)):
    
    if total[i] not in '1234567890':
        flag = False
        break
    
    if 0 <= int(total[i]) < 9 and (s in n[3] and s in n[7] or (s in n[1] and n[0] == '7')):
        flag = True
        
    else:
        flag = False
        break
    
if flag == True:
    print('YES')
else:
    print('NO')