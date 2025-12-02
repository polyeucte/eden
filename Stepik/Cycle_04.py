a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (0, 0, 0, 0) < (a, b, c, d) < (11, 11, 11, 11) and a <= b and c <= d:
    print('\t', end='')
    for i in range(c, d + 1):
        print(i, '\t', end='')
    print('')
    for j in range(a, b + 1):
        print(j, '\t', end='')
        for k in range(c, d + 1):
            print(j * k, '\t', end='')
        print('')
