# Задание №7
# 📌 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# 📌 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# 📌 Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# 📌 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# 📌 Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['is_leap_year', 'check_date_func']

def is_leap_year(year: int) -> bool:    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def check_date_func(date2check) -> bool:
    day, month, year = map(int, date2check.split('.'))    
    return (1 <= year <= 9999) and ( (1 <= day <= 31 and month in (1, 3, 5, 7, 8, 10, 12)) or (1 <= day <= 30 and month in (4, 6, 9, 11)) or
                                     (1 <= day <= 29 and month == 2 and is_leap_year(year)) or (1 <= day <= 28 and month == 2 and not is_leap_year(year)))


if __name__ == '__main__':         
    date_ = '30.02.2024'
    print(check_date_func(date_))
