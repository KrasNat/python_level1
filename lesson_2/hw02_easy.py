# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.




# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
 
list_fruits = ["яблоко", "банан", "киви", "арбуз"]

for num, fruit in enumerate (list_fruits):
	print (str(num) + '.  {:>10}'.format(fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = {1,2,30,7,20}
second_list = {3,50,1,7}
final_list = first_list - second_list
print ('Первый список: ', first_list) 
print ('Второй список: ', second_list)
print ('Список без элементов из второго: ',final_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [4,6,7,8,25,45,66,34]
print (numbers)
new_numbers = []
idx = 0
while idx != len(numbers)
if numbers[i]%2 == 0:
	numbers[i]*4
	lst.append(new_numbers)
	else :
	numbers[i]*2
	lst.append(new_numbers)
	idx += 1
print (new_numbers)		
