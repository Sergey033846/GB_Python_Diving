# Задание №7
# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

s = 'Пользователь вводит строку текста.'

# не используем count
dict_without_count = {}

# решение 1
# for char in s:
#     if char not in dict_without_count:
#         dict_without_count[char] = 1
#     else:
#         dict_without_count[char] += 1

# решение 2
for char in s:
    dict_without_count[char] = dict_without_count.get(char, 0) + 1

# используем count
dict_with_count = {}

for char in set(s):
    dict_with_count[char] = s.count(char)

# выводим оба списка и сравниваем
print('dict_without_count:')
print(dict_without_count)
print('dict_with_count:')
print(dict_with_count)
