# Задание №5
# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка, умноженная на процент премии.

from decimal import Decimal

names = ['Петр', 'Алексей', 'Иван']
salary = [15_000, 20_000, 50_000]
bonus = ['10.25', '5', '20']


def get_bonus_dict(names_list: list, salary_list: list, bonus_list: list) -> dict:
    dict_1 = {}

    for i, name_ in enumerate(names_list):
        dict_1[name_] = Decimal(salary_list[i]) * Decimal(bonus_list[i]) / 100

    return dict_1


print(get_bonus_dict(names, salary, bonus))
