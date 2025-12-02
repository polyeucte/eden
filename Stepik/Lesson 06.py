n = int(input())
x10 = n % 10
x100 = n % 100
if n < 0 or n > 1000:
    print('Вы ввели неверное значение!')
elif x10 == 1 and x100 != 11:
    print(n, 'программист')
elif (x10 in (2, 3, 4)) and (x100 not in (12, 13, 14)):
    print(n, 'программиста')
else:
    print(n, 'программистов')
