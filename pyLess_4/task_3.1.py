units = (
        u'ноль',
        (u'один', u'одна'),
        (u'два', u'две'),
        u'три', u'четыре', u'пять',
        u'шесть', u'семь', u'восемь', u'девять')
        
teens = (
        u'одиннадцать',
        u'двенадцать', u'тринадцать',
        u'четырнадцать', u'пятнадцать',
        u'шестнадцать', u'семнадцать',
        u'восемнадцать', u'девятнадцать',
        )

tens = (
        u'десять', u'двадцать', u'тридцать',
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


'''nxtNum = num
    res = []
    while nxtNum > 0:
        if nxtNum < 100:
            if nxtNum < 20 and nxtNum >= 10:
                res.insert(0, teens[nxtNum - 11])
                break
            else:
                nxtNum %= 10
                res.insert(0, units[nxtNum%10])
                nxtNum //= 10
        else:
            int(str(nxtNum)[1:])) < 20 & (int(str(nxtNum)[1:])) > 10
            res.insert(0, teens[int(str(nxtNum)[1:]) - 11])
            nxtNum //= 100
        
    
    res += f"{units[numAbs%1000]} 
    res += f"{''.join( orders[cntOrder - 1][0][0], ).strip()} '''


''' cntOrder = int(len(str(num)) // 3 - 1)
    while numAbs > 0:
        cntOrder -= 1
        if numAbs % 1000 != 0:
            
            nxtEl = trnslt2text(next3Dig, int(len(str(num)) // 3) - 1)
        numAbs //= 1000'''

