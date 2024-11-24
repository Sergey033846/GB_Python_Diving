# Домашнее задание 2
# Пакет для работы с файлами 1
# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него функцию rename_files

import os

with open('__init__.py', 'w', encoding='utf-8') as f:
    list4fill = ['import os', '__all__ = ["rename_files"]', 'def rename_files()']
    f.writelines('\n'.join(list4fill))


# решение автотеста
code_to_write = '''
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    files = os.listdir('geekbrains')

    filtered_files = [file for file in files if file.endswith(source_ext)]

    filtered_files.sort()

    num = 1

    for file in filtered_files:
        name = os.path.splitext(file)[0]

        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        os.rename(file, new_name)

        new_names.append(new_name)

        num += 1

    return new_names
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
