# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def is_prime_number(k: int) -> bool:
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True


def get_n_prime_numbers(m: int):
    number = 2
    counter = m
    while counter > 0:
        if is_prime_number(number):
            counter -= 1
            yield number
        number += 1


n = 13
print(*get_n_prime_numbers(n))
