x = int(input())
y = []
for i in range(1, x + 1):
    y.append(i)
lst = [[i for y in range(i)] for i in y]
result = []
for e in lst:
    if type(e) is list:
        result += e
    else:
        result.append(e)
print(*result[:x])
