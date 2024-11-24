# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и строку. 
# Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.


import argparse


def process_args(arg1, arg2, verbose=False, repeat=1):
    if verbose:
        print(f"arg1: {arg1}, arg2: {arg2}")
        print(f"Повторить строку {repeat} раз:")

    for _ in range(repeat):
        print(arg2)


if __name__ == "__main__":
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Обработка аргументов командной строки.')
    

    # Добавление аргументов
    parser.add_argument('number', type=int, help='Аргумент - целое число')
    parser.add_argument('string', type=str, nargs='*', help='Аргумент - строка')
    

    # Добавление опций
    parser.add_argument('--verbose', action='store_true', help='Включить подробный вывод')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
    

    # Парсинг аргументов
    args = parser.parse_args()
    
    
    if args.verbose:
        print(f'arg1: {args.number}, arg2: {' '.join(args.string)}, repeat: {args.repeat}')

    print(f'Число: {args.number}, Строка: {' '.join(args.string) * args.repeat}')