# Задание №3
# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

tuple1 = (1, 2.5, 2, 6, 'qwerty', [1, 2, 3], 'abcde')

dict1 = {}

for item in tuple1:
    if type(item) not in dict1:
        dict1[type(item)] = [item]
    else:
        dict1[type(item)].append(item)

print(dict1)
