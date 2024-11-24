# Задание №1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
# - от 1 до 100 для загадывания,
# - от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток. 

def guess_number():    
    number = int(input('Загадайте число (от 1 до 100): '))
    attempts = int(input('Введите количество попыток (от 1 до 10): '))

    def guessing():        
        nonlocal number, attempts
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
                
    return guessing


guess_func = guess_number()
guess_func()
