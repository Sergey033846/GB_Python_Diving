# Задание №5
# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.

list1 = [1, 2, 3, 4, 0,
         5, 6, 7, 8, 9,
         1, 2, 3, 4, 0,
         5, 6, 7, 8, 9,
         1, 2, 3, 4, 0]

list2 = []
for i, item in enumerate(list1):
    if item % 2:
        list2.append(i + 1)

print(list2)