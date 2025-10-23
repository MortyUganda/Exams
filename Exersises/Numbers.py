n = int(input())

strings = []
for _ in range(n):
    s = input()
    strings.append(s)

strings2 = []
txt = []

k = int(input())
for _ in range(k):
    search = input()
    strings2.append(search)

for j in strings:
    cnt = 0
    for i in range(k):
        if str(strings2[i]).upper() in str(j).upper():
            cnt += 1
            if cnt == (k):
                txt.append(j)
print(*txt, sep="\n")