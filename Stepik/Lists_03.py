a = [int(i) for i in input().split()]
a.sort()
index = 1
result = []
for n in a[:-1]:
    if n == a[index] and n not in result:
        result.append(n)
    index += 1
print(*result)
