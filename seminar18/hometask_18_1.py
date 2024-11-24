# ДЗ 1
# Генерация случайных данных и нахождение корней квадратного уравнения
# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, 
# и записывать их в CSV-файл. 
# Функция принимает два аргумента:
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.

# Функция принимает три аргумента:
# a, b, c (целые числа) - коэффициенты квадратного уравнения.

# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. 
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. 
# Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация 
# о параметрах и результатах вычислений для каждой строки данных из CSV-файла.


from typing import Callable
import json
import random as rnd
import csv


def save_to_json(func: Callable):        
    def wrapper(*args, **kwargs):        
        roots_list = []
        with open(args[0], 'r', newline='', encoding='utf-8') as fcsv:                
            csv_reader = csv.DictReader(fcsv, fieldnames=['a', 'b' ,'c'])        
            for koefs in csv_reader:                
                result = func(*map(int, koefs.values()))
                roots_list.append({'parameters': list(koefs.values()), 'result': result})                
        with open('seminar18/results.json', 'w', encoding='utf-8') as fjson:        
            json.dump(roots_list, fjson, indent=4)                    

    return wrapper


def generate_csv_file(file_name, rows):
    koefs_list = []
    for _ in range(rows):
        koefs_list.append({'a': rnd.randint(1, 50), 'b': rnd.randint(1, 50), 'c': rnd.randint(1, 50)})

    with open(file_name, 'w', newline='', encoding='utf-8') as fcsv:                
        csv_writer = csv.DictWriter(fcsv, fieldnames=['a', 'b' ,'c'])        
        csv_writer.writerows(koefs_list)

@save_to_json
def find_roots(a, b, c):        
    d = b * b - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b + d**0.5)/(2 * a), (-b - d**0.5) / (2 * a)


if __name__ == '__main__':
    generate_csv_file('seminar18/koefs.csv', 101)
    find_roots('seminar18/koefs.csv')


# решение автотеста
# import csv
# import json
# import random

# def save_to_json(func):
#     def wrapper(*args):
#         result_list = []
#         with open(args[0], 'r') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 a, b, c = map(int, row)
#                 result = func(a, b, c)
#                 data = {'parameters': [a, b, c], 'result': result}
#                 result_list.append(data)
#         with open('results.json', 'w') as f:
#             json.dump(result_list, f)
#     return wrapper

# @save_to_json
# def find_roots(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         return None
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         return x1, x2

# def generate_csv_file(file_name, rows):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         for i in range(rows):
#             row = [random.randint(1, 1000) for _ in range(3)]
#             writer.writerow(row)


