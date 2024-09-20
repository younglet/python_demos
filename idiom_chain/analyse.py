from load import idioms

res = []

for idiom in idioms:
    word = idiom['word']
    if len(word) != 4:
        continue
    a, b, c, d = word
    if a!=b and b!=c and c!=d and a==d:
        res.append(word)

print(res)