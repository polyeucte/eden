lst = input().split()
x = input()
if lst.count(x) == 0:
    print("Отсутствует")
else:
    ind = 0
    for i in lst:
        if i == x:
            print(lst.index(x, ind), end=" ")
        ind += 1
