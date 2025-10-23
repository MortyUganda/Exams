n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
res = int(input())
l = 0
r = len(num) - 1
res_res = "НЕТ"
while l != r:
    if num[l] * num[r] > res:
        r -= 1
    elif num[l] * num[r] < res:
        l += 1
    else:
        res_res = "ДА"
        break
print(res_res)
