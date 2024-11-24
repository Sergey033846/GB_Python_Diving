# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

MAXN: int = 100

even_numbers_with_sum8 = (i for i in range(MAXN + 1) if i % 2 == 0)
even_numbers_without_sum8 = (i for i in range(MAXN + 1) if i % 2 == 0 and sum(map(int, str(i))) != 8)

print(*even_numbers_with_sum8)
print(*even_numbers_without_sum8)
