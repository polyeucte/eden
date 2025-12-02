while True:
    a = int(input())
    if a > 100 and a != 100:
        break
    elif a < 10 and a != 10:
        continue
    print(a)
