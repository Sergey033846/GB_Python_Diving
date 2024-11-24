# Задание №6
# 📌 Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.


from typing import Callable
import json
import random as rnd
import os
from functools import wraps 


def count(num: int = 1):
    def deco(func: Callable): 
        @wraps(func)       
        def wrapper(*args, **kwargs): 
            for i in range(num):
                print(f'Итерация #{i + 1}')
                func(*args, **kwargs)

        return wrapper    
    return deco


def save2json(func: Callable):        
    @wraps(func)       
    def wrapper(*args, **kwargs):        
        result = func(*args, **kwargs)       

        dict1 = dict()   
        
        path_ = os.path.join(os.getcwd(), f'{func.__name__}.json')

        # читаем ранее созданный json-файл        
        if os.path.exists(path_):
            with open(path_, 'r', encoding='utf-8') as fjson:        
                dict1 = json.load(fjson)                
        
        # вносим изменения        
        dict1[str(result)] = {'args': args, 'kwargs': kwargs}
                
        # сохраняем измененный json-файл
        with open(path_, 'w', encoding='utf-8') as fjson:        
            json.dump(dict1, fjson, indent=4, ensure_ascii=False)        

        return result
    
    return wrapper


def enter_and_check_number_and_attempts(func: Callable):        
    @wraps(func)       
    def wrapper(*args, **kwargs):
        number, attempts, *_ = args        
        if not 1 <= number <= 100:
            number = rnd.randint(1, 100)
        if not 1 <= attempts <= 10:
            attempts = rnd.randint(1, 10)
        print(f'Загаданное число: {number}')        # для отладки
        print(f'Количество попыток: {attempts}')
        
        return func(number, attempts)        
                        
    return wrapper


@count(3)
@save2json
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
        return {number: -1}
    return {number: attempt}


guessing(23, 3)
