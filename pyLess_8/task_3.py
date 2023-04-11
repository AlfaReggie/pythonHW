"""Даны два слова и словарь. Требуется построить цепочку слов от первого слова до
второго, в котором каждые два соседних слова принадлежат словарю и отличаются
только в одной букве.
мел
рот
мел
мир
МОЛ
мот
ров
рот
сон
"""


def count_words_dif(a, b):
    count = 0
    for char_a in a:
        if char_a in b:
            count += 1
    return count


start = "мел"
finish = "рот"
words = ["мел",
         "мир",
         "мол",
         "мот",
         "ров",
         "рот",
         "сон"]
res = []

current = start
count = len(words)
while True:
    if current == finish or count < 0:
        break
    for i in range(len(words) - 1):
        if count_words_dif(current, words[i]) == 2 or start == words[i]:
            current = words[i]
            res.append(words.pop(i))
            break
    count -= 1
print(res)
