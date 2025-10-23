s = []
for el in input().split(" "):
    s.append(int(el))

s2 = []

while s:
    mn = min(s)
    mn_ind = s.index(min(s))
    s2.append(mn)
    del s[mn_ind]

s3 = []
s3 = s2[::-1]

print(*s2)
print(*s3)