__author__ = 'Канцеров Александр Павлович'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list_1 = [10, "asd", True, -15, "sdf", 12.7, False, 123, [1, 3]]			
			
list_for_number = []			
for i in list_1:			
    if isinstance(i, int) and type(i) != bool and i >= 0:			
        list_for_number.append(i)			
    else:			
        print("не подходит:", i)			
print(list_for_number)			





# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

from datetime import *
import locale
locale.setlocale(locale.LC_ALL, "ru")
date = '02.11.2013'

date_total = datetime.date(datetime.strptime(date, '%d.%m.%Y'))
date_total2 = date_total.strftime('%A %B %Y ' + "года")
print(date_total2)
