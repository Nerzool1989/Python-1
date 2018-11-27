# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    buf = []
    last = 0
    following = 1
    while True:
        if following <= m:
            buf.append(following)
        else:
            break
        last, following = following, following + last

    res = []
    for i in buf:
        if i < n:
            res.append(i)
    return res

print(fibonacci(40, 4000))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    buf = origin_list.copy()
    for passnum in range(len(buf) - 1, 0, -1): 
        for i in range(passnum):
           if buf[i] > buf[i + 1]:
                buf[i], buf[i + 1] = buf[i + 1], buf[i]
    return buf

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.