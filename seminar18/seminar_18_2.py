# Задание №2
# 📌 Дорабатываем задачу 1. 
# 📌 Превратите внешнюю функцию в декоратор. 
# 📌 Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. 
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.


from typing import Callable
import random as rnd


def enter_and_check_number_and_attempts(func: Callable):        
    def wrapper(*args, **kwargs):
        number, attempts, *_ = args        
        if not 1 <= number <= 100:
            number = rnd.randint(1, 100)
        if not 1 <= attempts <= 10:
            attempts = rnd.randint(1, 10)
        print(f'Загаданное число: {number}')        # для отладки
        print(f'Количество попыток: {attempts}')
        
        func(number, attempts)        
                        
    return wrapper


@enter_and_check_number_and_attempts
def guessing(number, attempts):                
    attempt = 1        
    while attempt <= attempts:
        yournumber = int(input(f'Попытка номер {attempt}. Введите число от 1 до 100: '))
        if (yournumber > number):
            print('Мое число меньше')
        elif (yournumber < number):
            print('Мое число больше')
        elif (yournumber == number):
            print(f'Вы угадали число с {attempt} попытки!')
            break 
        attempt += 1
    else:
        print('Вы проиграли. Ваши попытки закончились.')


#number_ = int(input('Загадайте число (от 1 до 100): '))
#attempts_ = int(input('Введите количество попыток (от 1 до 10): '))    
#guessing(number_, attempts_)
guessing(23, 3)
