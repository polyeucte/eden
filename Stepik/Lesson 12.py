x = int(input())
mtx = [[0 for i in range(x)] for j in range(x)]

row = 0
col = 0

for i in range(1, x + 1):
    mtx[row][col] = i
    col += 1

row += 1

for i in range(x + 1, x * x + 1):
    mtx[row][col] = i

# for i in range(1, x * x+1):
#     for right in range(x):
#         mtx[row][col] = i
#         col += 1

# print(mtx)

for i in mtx:
    print(i)

# for row in range(len(mtx)):
#    for col in range(len(mtx[row])):
#        print(mtx[row][col])
