a = int(input())
b = int(input())
s = 0
u = 0
for i in range(a, b+1):
    if (i % 3) == 0:
        s += i
        u += 1
print(s / u)
