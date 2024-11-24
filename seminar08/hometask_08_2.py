# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#
# Пример использования.
# На входе:
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
#
# На выходе:
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

def key_params(**kwargs) -> dict:
    dict_1 = dict()
    for key, value in kwargs.items():
        #key_dict_1 = str(value) if isinstance(value, list | dict | set) else value

        # исправлено для автотеста Python 3.8
        key_dict_1 = str(value) if isinstance(value, (list, dict, set)) else value

        # если несколько одинаковых значений аргументов (убрал для автотеста)
        #dict_1[key_dict_1] = list(dict_1[key_dict_1]) + [key] if key_dict_1 in dict_1 else key
        dict_1[key_dict_1] = key
    return dict_1


#params = key_params(a=1, b='hello', c=[1, 2, 3], d={}, e=1, bcd=1)
params = key_params(a=True, b=False, c=True, d=False)
print(params)

# решение автотеста
# def key_params(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if value is None:
#             result[value] = key
#         elif isinstance(value, (int, str, float, bool, tuple)):
#             result[value] = key
#         else:
#             result[str(value)] = key
#     return result

