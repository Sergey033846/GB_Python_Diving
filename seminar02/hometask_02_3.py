# Лотерея
# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Числа в каждом списке не повторяются.
#
# Пример входных данных:
# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
#
# Пример выходных данных:
# Количество совпадающих чисел: 7

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

count = 0

for i in list1:
    for j in list2:
        if i == j:
            count += 1

print(f'Количество совпадающих чисел: {count}')

# решение автотеста
# count = 0
#
# for num1 in list1:
#     if num1 in list2:
#         count += 1
#
# print(f"Количество совпадающих чисел: {count}")
