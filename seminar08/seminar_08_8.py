# Задание №8
# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

s = 'one_s'
int1s = 4
int1 = 'ints_value'
str1s = 'strs_value'
str1 = 'something'


def change_values_for_vars_ending_on_s():
    dict_globals = globals()
    for var in dict_globals:
        if var.endswith('s') and var != 's':
            var_without_s = var.removesuffix('s')
            if var_without_s in dict_globals:
                dict_globals[var_without_s] = dict_globals[var]
            dict_globals[var] = None


print('Было:')
print(f'{s = }, {int1s = }, {int1 = }, {str1s = }, {str1 = }')

change_values_for_vars_ending_on_s()

print('Стало:')
print(f'{s = }, {int1s = }, {int1 = }, {str1s = }, {str1 = }')
