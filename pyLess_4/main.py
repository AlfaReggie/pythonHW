units = (
        u'ноль',
        (u'один', u'одна'),
        (u'два', u'две'),
        u'три', u'четыре', u'пять',
        u'шесть', u'семь', u'восемь', u'девять')

teens = (
        u'десять', u'одиннадцать',
        u'двенадцать', u'тринадцать',
        u'четырнадцать', u'пятнадцать',
        u'шестнадцать', u'семнадцать',
        u'восемнадцать', u'девятнадцать')

tens = (
        teens,
        u'двадцать', u'тридцать',
        u'сорок', u'пятьдесят',
        u'шестьдесят', u'семьдесят',
        u'восемьдесят', u'девяносто')

hundreds = (
        u'сто', u'двести',
        u'триста', u'четыреста',
        u'пятьсот', u'шестьсот',
        u'семьсот', u'восемьсот',
        u'девятьсот')

orders = (
        ((u'тысяча', u'тысячи', u'тысяч'), 'f'),
        ((u'миллион', u'миллиона', u'миллионов'), 'm'),
        ((u'миллиард', u'миллиарда', u'миллиардов'), 'm'),
        ((u'дохреллиард', u'дохреллиарда', u'дохреллиардов'), 'm'),)

minus = u'минус'


def thousand(rest, sex):
    prev = 0  # последняя обработанная часть числа
    plural = 2  # параметр формы слова (одна тысяча, две тысячи, три тысячи, четыре тысячи, пять тысяч...)
    name = []  # список для накопления числа прописью
    use_teens = rest % 100 >= 10 and rest % 100 <= 19  # Отсекаем правые 2 числа, проверяем вхождение в диапазон [10, 20)
    if not use_teens:  # если правые 2 числа не входят в диапазон, то используем кортеж 'tens'
        data = ((units, 10), (tens, 100), (hundreds, 1000))  # создаем кортеж с наборами имен и параметром отсекания числа 
    else:  # иначе используем кортеж 'teens'
        data = ((teens, 10), (hundreds, 1000))  # создаем кортеж с наборами имен и параметром отсекания числа
    for names, x in data:  # здесь 'names' – это набор имен, а 'x' – позиция числа, которому будет присвоено имя
        cur = int(((rest - prev) % x) * 10 / x)  # странный подход, как по мне, ну ладно... от переданного в функцию числа 'rest' отнимаем уже обработанную его часть 'prev', отсекаем позицию числа для транслирования его прописью составной операцией "... % x * 10"
        prev = rest % x  # в 'prev' сохраняем отработанную часть числа на данном этапе
        if x == 10 and use_teens:  # если текущий разряд "десятки" и используем кортеж 'teens'
            plural = 2
            name.insert(0, teens[cur])  # добавляем число прописью в начало формируемой строки
        elif cur == 0:  # если в текущем разряде числа 0, то пропускаем итерацию
            continue  # то пропускаем итерацию
        elif x == 10: # если текущий разряд "десятки"
            name_ = names[cur]  # копируем кортеж 'nemes[cur]' в переменную 'name_'
            if isinstance(name_, tuple):  # если 'name_' является кортежем.
                name_ = name_[0 if sex == 'm' else 1]  # если род мужской, то берем 1-й элемент, иначе 2-й
            name.append(name_)  # добавляем имя группы разрядов числа в конец формируемой строки
            if cur >= 2 and cur <= 4:  # определяем значение параметра формы слова
                plural = 1
            elif cur == 1:
                plural = 0
            else:
                plural = 2
        else:
            name.append( names[cur-1])  # добавляем в конец имя группы разрядов
        
    return plural, name


def num2text(num, main_units=((u'', u'', u''), 'm')):
    """ Функция собирает строку в соответсвии с необходимым порядком разрядов. Строку собирет функция thousand() вызываемая из этого блока кода.
    """
    _orders = (main_units,) + orders
    if num == 0:
        return ''.join(units[0],)

    rest = abs(num)
    ord = 0
    name = []
    while rest > 0:
        plural, nme = thousand(rest % 1000, _orders[ord][1])
        if nme or ord == 0:
            name.append(_orders[ord][0][plural])
        name += nme
        rest = int(rest / 1000)
        ord += 1
    if num < 0:
        name.append(minus)
    name.reverse()
    return ' '.join(name).strip()


def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

print(num2text(checkInput("Enter number: ")))