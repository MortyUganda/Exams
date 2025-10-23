# Упаковка дубликатов 🌶️
n = input().split()
k = int(input())

print([n[i:i+k] for i in range(0, len(n), k)])