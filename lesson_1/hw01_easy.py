
__author__ = 'Красовская Наталья'

# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

number = input('Введите число ')
i = 0
while i < len(number):
	print(number[i])
	i += 1


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

first = input('Введите первое значение: ')
second = input('Введите второе значение: ')
temporary = first
first = second
second = temporary
print(first,second)



# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = input('Введите ваш возраст: ')
if int(age) >= 18:
	print('Доступ разрешен')
else:
	print('Извините, пользование данным ресурсом только с 18 лет')
