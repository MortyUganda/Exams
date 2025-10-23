age = int(input())

if 0<= age <= 13:
    print("детство")

if 14 <= age <= 24:
    print("молодость")

if 25 <= age <= 59:
    print("зрелость")

if age >= 60:
    print("старость")
else:
    print('не верно введен возраст')