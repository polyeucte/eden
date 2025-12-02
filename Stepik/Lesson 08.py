x = int(input())
y = x
z = x * x
while y != 0:
    x = int(input())
    y = x + y
    z += x * x
print(z)
