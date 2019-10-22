# Квадратное уравнение - 1
'''
Даны действительные коэффициенты a, b, c, при этом a != 0.
Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
Формат ввода
Вводятся три действительных числа.
Формат вывода
Если уравнение имеет два корня, выведите два корня в порядке возрастания,
если один корень — выведите одно число, если нет корней — не выводите ничего.
'''
import math
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (- b - math.sqrt(d)) / (2 * a)
    x2 = (- b + math.sqrt(d)) / (2 * a)
    if x1 < x2:
        print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
    else:
        print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
elif d == 0:
    x1 = - b / (2 * a)
    print('{0:.6f}'.format(x1))
