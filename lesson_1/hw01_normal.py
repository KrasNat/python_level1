
__author__ = 'Красовская Наталья'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.

number = input('Введите произвольное целое число: ')
print(max(number)) 


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
a = int(input('Введите первое число: '))
b = int(input ('Введите второе число: '))
a = a + b;
b = b - a;
b = -b;
a = a - b;
print (a,b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input('Введите число a: '))
b = int(input ('Введите число b: '))
c = int(input ('Введите число c: '))
x = int(input ('Введите число x: '))
D = int(b ** 2 — 4 * a * c)
if D > 0:
	print ('Первый корень: ', (-b - math.sqrt(D)) / 2 * a))
	print ('Первый корень: ', (-b + math.sqrt(D)) / 2 * a))
elsif D = 0:
	print ('Корень равен: ', (-b / (2 * a))
elseif D < 0:
	print ('Действительных корней нет')		