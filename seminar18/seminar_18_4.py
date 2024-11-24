# Задание №4
# 📌 Создайте декоратор с параметром. 
# 📌 Параметр - целое число, количество запусков декорируемой функции. 


from typing import Callable

def count(num: int = 1):
    def deco(func: Callable):        
        def wrapper(*args, **kwargs): 
            for i in range(num):
                print(f'Итерация {func(*args, **kwargs)} #{i + 1}')

        return wrapper    
    return deco


@count(5)
def func1():   
    return 'func1'


func1()
