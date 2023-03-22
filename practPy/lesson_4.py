text = ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']

newList = []
for i in range(len(text)):
    if text[:i].count(text[i]) != 0:
        newList.append(f'{text[i]}_{text[:i].count(text[i])}')
    else:
        newList.append(text[i])

print(newList)

