DNA = input()
test = DNA[0]
out = ''
s = 0
for p in DNA:
    if p != test:
        out += test + str(s)
        s = 1
        test = p
    else:
        s += 1
        test = p
print(out + test + str(s))
