lst_words = [input().lower() for _ in range(int(input()))]
    
lst_wrong_words = []
for i in range(int(input())):
    sentence = [lst_wrong_words.append(el) for el in input().lower().split() if el not in lst_words]
    
print(lst_words)
print(*set(lst_wrong_words), sep="\n")