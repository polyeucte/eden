n = int(input())
abc = n // 1000
a = abc // 100
b = (abc % 100) // 10
c = abc % 10
xyz = n % 1000
x = xyz // 100
y = (xyz % 100) // 10
z = xyz % 10
if (a + b + c) == (x + y + z):
    print('Счастливый')
else:
    print('Обычный')
