# Проценты
'''
Процентная ставка по вкладу составляет P процентов годовых,
которые прибавляются к сумме вклада.
Вклад составляет X рублей Y копеек.
Определите размер вклада через год.
При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
'''
p = int(input())
x = int(input())
y = int(input())
deposit = x + y / 100
perc = 1 + p / 100
deposit = deposit * perc
rub = int(deposit)
x = deposit - int(deposit)
kop = int(float('{0:.10}'.format(x)) * 100)
print(rub, kop)
