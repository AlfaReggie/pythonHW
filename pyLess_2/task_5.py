'''***(2)У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке.
 Вы можете вставлять между ними знаки «+», «-» или ничего.
 У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.'''


def allCombinations(a):  #создание функции для создания всех комбинаций чисел
    if len(a) <= 1: #проверка условия на конец списка чисел
        yield a
    else:
        head = '' #создаем пустую строку для хранения получившейся комбинации

        tail = list(a) #передаем в переменную уменьшающийся список
        while len(tail) > 0: #проходимся по дублирующимся уменьшающимся спискам
            head += tail.pop(0) #добавляем новое число как строку
            for s in allCombinations(tail): # рекурсия для прохода по оставшемуся количеству элементов списка
                yield [head] + s

def allSigns(n): #функция формирования знаков сложения и вычитания между количеством очередной строки
    if n == 0:
        yield()
    else:
        for tail in allSigns(n - 1):
            for s in '+-':
                yield (s,) + tail


def performOperations(nums, signs): # результирующая функция для очередного вывода функций формирования числа и знака
    nums = list(map(int, nums))
    result = nums.pop(0)
    for s in signs:
        if s == '+':
            result += nums.pop(0)
        if s == '-':
            result -= nums.pop(0)
    return result


for numbers in allCombinations(tuple(map(str, range(1, 10)))):

    for signs in allSigns(len(numbers) - 1):

        summ = performOperations(numbers, signs)
        if summ == 100:
            print(
                ''.join(map(
                    lambda x: ''.join(x),
                    zip(numbers, signs)))
                + numbers[-1])

