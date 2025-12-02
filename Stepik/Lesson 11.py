mtx = [[int(i) for i in input().split()]]
X = input()
while X != 'end':
    mtx.append([int(i) for i in X.split()])
    X = input()
for row in range(len(mtx)):
    for col in range(len(mtx[row])):
        if row == len(mtx) - 1 and len(mtx) != 1:
            row = -1
        if col == len(mtx[row]) - 1 and len(mtx[row]) != 1:
            col = -1
        if len(mtx) != 1 and len(mtx[row]) != 1:
            print((mtx[row - 1][col] + mtx[row + 1][col]) + (mtx[row][col - 1] + mtx[row][col + 1]), end=' ')
        elif len(mtx) == 1 and len(mtx[row]) == 1:
            print((mtx[0][0]) * 4)
        elif len(mtx) == 1 and len(mtx[row]) != 1:
            print((mtx[row][col] + mtx[row][col]) + (mtx[row][col - 1] + mtx[row][col + 1]), end=' ')
        elif len(mtx) != 1 and len(mtx[row]) == 1:
            print((mtx[row - 1][col] + mtx[row + 1][col]) + (mtx[row][col] + mtx[row][col]), end=' ')
    print()
