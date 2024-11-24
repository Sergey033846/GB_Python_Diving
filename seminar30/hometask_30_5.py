# Задача 5. Запуск из командной строки
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. 
# Каждый объект хранит: 
# - имя файла без расширения или название каталога, 
# - расширение, если это файл, 
# - флаг каталога, 
# - название родительскогокаталога. 
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import os
import logging
import argparse
from collections import namedtuple


logging.basicConfig(filename='dir_info.log', level=logging.INFO, format='%(asctime)s - %(message)s', encoding='utf-8')


DirectoryInfo = namedtuple('DirInfo', ['name', 'extension', 'is_dir', 'parent'])
                           

# Реализуем рекурсивный обход каталога
def get_dir_info(directory_path):
    directory_info = []
    
    for item in os.scandir(directory_path):                
        name, extension = os.path.splitext(item)
        is_dir = item.is_dir()
        parent = directory_path
        
        directory_info.append(DirectoryInfo(name, extension, is_dir, parent))
        
        if is_dir:
            subdir_info = get_dir_info(os.path.join(directory_path, name))
            directory_info.extend(subdir_info)
    
    return directory_info


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Сбор информации о содержимом директории.')
    parser.add_argument('dir_path', type=str, help='Путь до директории')
    args = parser.parse_args()
    
    dir_path = args.dir_path
    
    if not os.path.isdir(dir_path):
        print('Ошибка: указанный путь не является директорией.')
        raise ValueError(f'Указанный путь {dir_path} не является директорией.')
    
    directory_info = get_dir_info(dir_path)
    
    for info in directory_info:
        logging.info(f'Имя: {info.name}, Расширение: {info.extension}, Каталог: {info.is_dir}, Родительский каталог: {info.parent}')


    # Пример использования
    # python hometask_30_5.py D:\Projects\GB\GB_Python_Diving