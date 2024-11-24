# ДЗ 2
# Пакет для работы с файлами 3
# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file


with open('__init__.py', 'w', encoding='utf-8') as f:
    list4fill = [
                 '__all__ = ["save_to_json", "find_roots", "generate_csv_file"]', 
                 'def save_to_json()',
                 'def find_roots()',
                 'def generate_csv_file()',
                 ]
    f.writelines('\n'.join(list4fill))

