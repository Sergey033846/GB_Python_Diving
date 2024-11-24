# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. 
# Дополнительно, выведите эту дату в формате YYYY-MM-DD.


from datetime import datetime, timedelta


def future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')


days_to_add = 7
print(f"Дата через {days_to_add} дней: {future_date(days_to_add)}")