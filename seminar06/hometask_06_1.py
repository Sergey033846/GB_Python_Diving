# Список вещей для похода
#
# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
#
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
#
# На входе:
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
# На выходе, например, один из допустимых вариантов может быть таким:
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}

from itertools import combinations, chain

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}

max_weight = 1.0

# Функция для генерации всех возможных комбинаций вещей
def generate_combinations(items, max_weight):
    combinations = set()  # Используем множество для хранения уникальных комбинаций
    for i in range(len(items) + 1):
        for combo in combinations_with_replacement(items.keys(), i):
            combo_weight = sum(items[item] for item in combo)
            if combo_weight <= max_weight:
                combinations.add(combo)  # Добавляем комбинацию в множество
    return combinations

# Функция для генерации комбинаций с повторениями
def combinations_with_replacement(items, r):
    return chain(*(combinations(items, i) for i in range(r + 1)))

# Генерация всех возможных комбинаций вещей, которые влезут в рюкзак
all_combinations = generate_combinations(items, max_weight)

# Преобразование множества обратно в список для сортировки и вывода результатов
all_combinations = list(all_combinations)

# Отсортировка списка по убыванию длин значений
all_combinations.sort(key=len, reverse=True)

# Создание словаря с вещами и их массой для каждой комбинации
results = []
for combo in all_combinations:
    combo_dict = {item: items[item] for item in combo}
    results.append(combo_dict)

# Вывод результатов
# for idx, result in enumerate(results):
#     total_weight = sum(result.values())
#     print(f"Вариант {idx + 1}: {result} - общая масса {total_weight} кг")

backpack = []
if len(results):
    backpack = results[0]

print(backpack)

# решение автотеста
# backpack = {}
#
# for item, weight in items.items():
#     if weight <= max_weight:
#         backpack[item] = weight
#         max_weight -= weight
