# Задание №8
# Нарисовать в консоли ёлку, спросив у пользователя количество рядов.

n = 5

for i in range(5):
    print(" " * (n - i - 1), '*' * (i * 2 + 1))