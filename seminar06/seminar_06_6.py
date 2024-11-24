# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

s = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'

words_list = sorted(s.split())

max_len = len(max(words_list, key=len))

for i, word in enumerate(words_list):
    print(f'{i + 1} {word:>{max_len}}')
