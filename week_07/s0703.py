# Встречалось ли число раньше
'''
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее
встречалось в последовательности или NO, если не встречалось.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
'''
list_01 = list(map(int, input().split()))
list_02 = []
set_01 = set(list_02)
for element in list_01:
    if element in set_01:
        print('YES')
    else:
        print('NO')
    set_01.add(element)
