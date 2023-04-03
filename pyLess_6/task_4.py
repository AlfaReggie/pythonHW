'''
Дано 20+ значное целое число, проверить его на делимость на 7

Ввод 234523642345789812354678654323454919865

Вывод Делится


'''

n = 234523642345789812354678654323454919865
diff = 10 ** round(len(str(n)) / 10)

def main(n, diff):
    if n <= diff:
        return n
    while n >= diff:
        #a = n % diff
        return main(n // diff + (n % diff * 2), diff)

if __name__ == "__main__":
    numberRes = main(n, diff)
    if numberRes % 7 == 0:
        print("Делится")
    else:
        print("Не делится")

