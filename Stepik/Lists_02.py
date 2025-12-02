a = [int(i) for i in input().split()]  # List Comprehension
result = []
left = -1
right = 1
if len(a) == 1:
    result.append(*a)
else:
    for n in a[:-1]:
        result.append(a[left] + a[right])
        left += 1
        right += 1
    result.append(a[-2] + a[0])
print(*result)
