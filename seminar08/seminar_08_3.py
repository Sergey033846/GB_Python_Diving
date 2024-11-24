# Задание №3
# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def get_Unicode_dict(s: str) -> dict:
    numbers = sorted(s.split())
    dict_1 = {chr(i): i for i in range(int(numbers[0]), int(numbers[1]) + 1)}
    return dict_1


s = '1105 1072'

print(get_Unicode_dict(s))
