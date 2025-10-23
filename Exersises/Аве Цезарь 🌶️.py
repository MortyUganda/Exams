n = input().split()
abc = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
c =[]
a = 26
x = 122
for i in range(len(n)):
    k = 0
    for j in range(len(n[i])):
        if n[i][j] in abc:
            k += 1
    for m in range(len(n[i])):
        if n[i][m] in abc:
            if ord(n[i][m].lower()) + k <= x:
                c.append(chr(ord(n[i][m])+k))
            else:
                c.append(chr(ord(n[i][m])+k-a))
        else:
            c.append(n[i][m])
    c.append(' ')
c = ''.join(c)
print(c)
