# Задание №2
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки, отсортированный по убыванию.

def get_Unicode_codes(s: str) -> list:
    set_1 = {ord(char) for char in s}
    return sorted(set_1, reverse=True)


s = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'

print(get_Unicode_codes(s))
