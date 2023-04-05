'''
Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(),
которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
В результате работы она выводит следующие данные: название анализируемой функции,
наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).
Попробуйте повторить результат девушки.

В данном случае на подмогу приходит модуль inspect. С его помощью можно реализовать задуманный функционал.

def my_func(a, b, /, c, d, *args, e, f, **kwargs):
pass

Анализируем функцию my_func
a: POSITIONAL_ONLY
b: POSITIONAL_ONLY
c: POSITIONAL_OR_KEYWORD
d: POSITIONAL_OR_KEYWORD
args: VAR_POSITIONAL
e: KEYWORD_ONLY
f: KEYWORD_ONLY
kwargs: VAR_KEYWORD
'''

import inspect

def inspect_function(some_func):
    print(f'Analysis function: {some_func.__name__}\n')
    print('-' * 30)
    params = ''
    for param in inspect.signature(some_func).parameters.values():
        params += (f"{param.name}: {param.kind}\n")
    return params

def my_func(a, b, /, c, d, *args, e, f, **kwargs):
    pass

print(inspect_function(my_func))
