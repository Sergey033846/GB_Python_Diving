# Задание №4
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.


list_1 = [5, 34, 2, 12, 9, 107, 8]


def bubble_sort(list_):
    for i in range(1, len(list_)):
        for j in range(len(list_) - i):
            if list_[j] > list_[j + 1]:
                temp = list_[j]
                list_[j] = list_[j + 1]
                list_[j + 1] = temp


print(f'{list_1=}')

bubble_sort(list_1)

print(f'{list_1=}')
