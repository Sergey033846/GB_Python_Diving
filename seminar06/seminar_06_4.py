# Задание №4
# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.
# таким образом, удаляем только "пары"

list1 = [1, 2, 3, 4, 0,
         5, 6, 7, 8, 9,
         1, 2, 3, 4, 0,
         5, 6, 7, 8, 9,
         1, 2, 3, 4, 0]

# через создание нового списка, если элемент встречается только дважды
# list2 = []
# for item in list1:
#     if list1.count(item) != 2:
#         list2.append(item)
# print(list2)

# удаляем из исходного пары элементов
i = 0

while i < len(list1):
    item = list1[i]
    count_n = list1.count(item)
    if count_n // 2:
        list1.remove(item)
        list1.remove(item)
        i = 0
    else:
        i += 1

print(f'{list1=}')
