# Домашнее задание 2
# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

# Создайте файл __init__.py и запишите в него все функции:
# get_dir_size,
# save_results_to_json,
# save_results_to_csv,
# save_results_to_pickle, traverse_directory.

with open('__init__.py', 'w', encoding='utf-8') as f:
    list4fill = ['import os', 
                 '__all__ = ["get_dir_size", "traverse_directory", "save_results_to_csv", "save_results_to_json", "save_results_to_pickle"]', 
                 'def get_dir_size()',
                 'def traverse_directory()',
                 'def save_results_to_json()',
                 'def save_results_to_csv()',
                 'def save_results_to_pickle()']
    f.writelines('\n'.join(list4fill))