with open("prices.txt", encoding="utf-8") as file:
    cnt = 0
    for line in file:
        temp = line.split()
        cnt += int(temp[1]) * int(temp[2])
    print(cnt)