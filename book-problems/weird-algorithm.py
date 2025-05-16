n = int(input())
list = [n]

while n != 1:
    if n % 2 == 0:
        n = n // 2
        list.append(n)
    else:
        n = n * 3 + 1
        list.append(n)

print(*list) #unpucking