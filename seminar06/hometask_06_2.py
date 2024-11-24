# Часто встречающиеся слова
#
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
#
# На входе:
# text = 'Hello world. Hello Python. Hello again.'
#
# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

# удаление знаков препинания
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#table = str.maketrans(" ", "_", string.punctuation)
#text = text.translate(table)

import string

# text = "Hello world. Hello Python. Hello again."

# text = 'This is a sample text without repeating words.'
# [('words', 1), ('without', 1), ('this', 1), ('text', 1), ('sample', 1), ('repeating', 1), ('is', 1), ('a', 1)]
#
# text = "Python 3.9 is the latest version of Python. It's awesome!"
# [('python', 2), ('version', 1), ('the', 1), ('s', 1), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)]
#
# text = 'Python is python, is, IS, and PYTHON.'
# [('python', 3), ('is', 3), ('and', 1)]
#
text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
# [('lazy', 3), ('the', 2), ('fox', 2), ('dog', 2), ('quick', 1), ('over', 1), ('jumps', 1), ('brown', 1)]

# моё решение
text = text.lower()

for literal_punctuation in string.punctuation:
    if literal_punctuation in text:
        text = text.replace(literal_punctuation, ' ')

words_list = text.split()
words_list.sort(reverse=True)

dict1 = dict()

for word in words_list:
    if not word.isdigit():
        word_count = words_list.count(word)
        if word_count in dict1:
            if word not in dict1[word_count]:
                dict1[word_count].append(word)
        else:
            dict1[word_count] = [word]

new_list = []

for key, words in sorted(dict1.items(), reverse=True):
    for word in words:
        new_list.append((word, key))

print(new_list[:10])

# решение автотеста
# import re
# from collections import Counter
#
# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
#
# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}
#
# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1
#
# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]
#
# print(top_words)
