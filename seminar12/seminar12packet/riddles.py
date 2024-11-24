# Задание №4
# 📌 Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Задание №5
# 📌 Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# 📌 Ключ словаря - загадка, значение - список с отгадками.
# 📌 Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Задание №6
# 📌 Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# 📌 Функция формирует словарь с информацией о результатах отгадывания.
# 📌 Для хранения используйте защищённый словарь уровня модуля.
# 📌 Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# 📌 Для формирования результатов используйте генераторное выражение.

__all__ = ['answer_all_riddles']


_results_all_riddles = dict()
ATTEMPTS_COUNT = 3


def answer_the_riddle(riddle: str, answers: list, attempts: int) -> bool:            
    print(f'Моя загадка: {riddle}. \nЧтобы её отгадать у тебя есть {attempts} попыток. Давай начнем!')
    answers = list(map(lambda x: x.lower(), answers))    
    for attempt in range(attempts):
        user_answer = input(f'Попытка № {attempt + 1}: ').lower()        
        if user_answer in answers:
            print(f'Ты угадал с {attempt + 1} попытки!')
            return attempt + 1
        else:
            print('Не угадал! Попробуй ещё!')
    return 0


def answer_all_riddles():    
    dict_riddles = {'первая планета от Солнца': ['Меркурий'], 
                    'вторая планета от Солнца': ['Венера'], }
    for riddle, riddle_answers in dict_riddles.items():
         add_riddle_result(riddle, answer_the_riddle(riddle, riddle_answers, ATTEMPTS_COUNT))        
    print_riddles_results()
    

def add_riddle_result(riddle: str, attempt: int) -> dict:
    global _results_all_riddles
    _results_all_riddles[riddle] = attempt    
    

def print_riddles_results():
    global _results_all_riddles
    print('Результаты соревнования:')
    for riddle, attempt in _results_all_riddles.items():
        print(f'Загадка "{riddle}": {f'попытка {attempt}' if attempt else 'Все попытки исчерпаны!'}')


if __name__ == '__main__':
    answer_all_riddles()
