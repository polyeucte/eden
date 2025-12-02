words_lst = []
words_dst = {}
while True:
    inp = input()
    if inp == ' ':
        break
    words_lst += inp.split()
for word in words_lst:
    txt_count = words_lst.count(word)
    words_dst[word] = txt_count

for key in words_dst:
    print(key, words_dst[key])
