bio = int(input())
it = int(input())
if bio >= it:
    MAX = bio
    MIN = it
elif it >= bio:
    MAX = it
    MIN = bio
d = MAX
while (d % MIN) != 0:
    d += MAX
print(d)
