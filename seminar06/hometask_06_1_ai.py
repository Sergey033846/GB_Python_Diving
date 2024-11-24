from itertools import combinations, chain

# things = {
#     'палатка': 2,
#     'спальник': 1.5,
#     'газа': 0.5,
#     'фонарик': 0.3,
#     'еда': 1,
#     'вода': 2,
#     'аптечка': 0.8,
#     'одежда': 1.2,
#     'книга': 0.4,
#     'телефон': 0.1
# }
#
# max_weight = 5

things = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}

max_weight = 1.0

# Функция для генерации всех возможных комбинаций вещей
def generate_combinations(things, max_weight):
    combinations = set()  # Используем множество для хранения уникальных комбинаций
    for i in range(len(things) + 1):
        for combo in combinations_with_replacement(things.keys(), i):
            combo_weight = sum(things[item] for item in combo)
            if combo_weight <= max_weight:
                combinations.add(combo)  # Добавляем комбинацию в множество
    return combinations

# Функция для генерации комбинаций с повторениями
def combinations_with_replacement(items, r):
    return chain(*(combinations(items, i) for i in range(r + 1)))

# Генерация всех возможных комбинаций вещей, которые влезут в рюкзак
all_combinations = generate_combinations(things, max_weight)

# Преобразование множества обратно в список для сортировки и вывода результатов
all_combinations = list(all_combinations)

# Отсортировка списка по убыванию длин значений
all_combinations.sort(key=len, reverse=True)

# Создание словаря с вещами и их массой для каждой комбинации
results = []
for combo in all_combinations:
    combo_dict = {item: things[item] for item in combo}
    results.append(combo_dict)

# Вывод результатов
for idx, result in enumerate(results):
    total_weight = sum(result.values())
    print(f"Вариант {idx + 1}: {result} - общая масса {total_weight} кг")