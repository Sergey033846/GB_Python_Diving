# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. 
# При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.


from typing import Callable
import json
import random as rnd
import os


def save2json(func: Callable):        
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


@save2json
def sum_args_kwargs(*args, **kwargs):
    '''суммируем все переданные параметры'''                    
    result = 0
    for item in args:
        result += int(item)
    for value in kwargs.values():
        result += int(value)
    return result


print(sum_args_kwargs(20))
print(sum_args_kwargs(25, "15", arg1 = 5, arg2 = "10"))
print(sum_args_kwargs(225, "215", arg1 = 25, arg2 = "20"))
