# Задание №6
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

from typing import Iterable

index = [0, 1, 2, 3, 4, 5, 6, 7, 8,  9,]
#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
list1 = [1, 2, 3, 4, ]
index1 = -10
index2 = 0


def sum_items_between(__iterable: Iterable, start_index: int, end_index: int):
    return sum(list1[start_index:end_index + 1])


print(sum_items_between(list1, index1, index2))
