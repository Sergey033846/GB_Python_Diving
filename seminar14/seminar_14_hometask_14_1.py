import os
import random as rnd
import shutil


__all__ = ['file_fill_int_float', 'file_generate_pseudonyms', 'file_multiply_and_rename', 
           'file_create_files_with_ext', 'file_create_files_with_several_ext', 'file_sort_files_by_dirs', 'rename_files']

# Задание №1
# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

def file_fill_int_float(filename, strcount):
    with open(filename, 'a', encoding='utf-8') as f:        
        list4fill = (f'{rnd.randint(-1000, 1000)}|{rnd.uniform(-1000, 1000)}\n' for _ in range(strcount))
        f.writelines(list4fill)


# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

def file_generate_pseudonym(min_len, max_len):
        vowels = 'aoeiuy'
        pseudonym = [chr(rnd.randrange(ord('a'), ord('z'))) for _ in range(rnd.randint(min_len - 1, max_len - 1))] + [rnd.choice(vowels)]
        rnd.shuffle(pseudonym)
        return ''.join(pseudonym).title()

def file_generate_pseudonyms(filename, pseudonyms_count):
    with open(filename, 'w', encoding='utf-8') as f:
        list4fill = (file_generate_pseudonym(4, 7) for _ in range(pseudonyms_count))
        f.writelines('\n'.join(list4fill))


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

def file_multiply_and_rename(filename, file_numbers, file_names):
    with (
        open(filename, 'w', encoding='utf-8') as fdest,
        open(file_numbers, 'r', encoding='utf-8') as fnums,
        open(file_names, 'r', encoding='utf-8') as fnames
        ):

        is_file_numbers_ending =  is_file_names_ending = False

        while not (is_file_numbers_ending and is_file_names_ending):
            nums_line = fnums.readline().replace('\n', '')
            name = fnames.readline().replace('\n', '')            

            if not nums_line:
                is_file_numbers_ending = True
                fnums.seek(0, 0)
                nums_line = fnums.readline().replace('\n', '')

            if not name:
                is_file_names_ending = True
                fnames.seek(0, 0)
                name = fnames.readline().replace('\n', '')

            if not (is_file_numbers_ending and is_file_names_ending):
                nums = list(map(float, nums_line.split('|')))
                multiply = nums[0] * nums[1]
                if multiply < 0:
                    print(f'{name.lower()},{abs(multiply)}', file=fdest)
                else:
                    print(f'{name.upper()},{round(multiply)}', file=fdest)


# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

def file_create_files_with_ext(ext, dir_, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files_count=42):
    path_ = os.path.join(os.getcwd(), dir_)
    if not os.path.exists(path_):
        os.mkdir(path_)        
    for _ in range(files_count):
        with open(os.path.join(os.getcwd(), dir_, f'{file_generate_pseudonym(min_len, max_len)}.{ext}'), 'bw') as f:
            f.write(os.urandom(rnd.randint(min_bytes, max_bytes)))
            

# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

def file_create_files_with_several_ext(exts_counts: dict, dir):
    for ext, file_count in exts_counts.items():
        file_create_files_with_ext(ext, dir, files_count=file_count)


# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

def file_sort_files_by_dirs(folder_exts: dict, dir_):
    current_path = os.path.join(os.getcwd(), dir_)    
    for dir_path, _, ﬁle_names in os.walk(current_path):        
        for file_name_src in file_names:            
            dir_dest = folder_exts.get(file_name_src.split('.')[1], False)
            if dir_dest:
                path_dest = os.path.join(current_path, dir_dest)
                if not os.path.exists(path_dest):
                    os.mkdir(path_dest)
                path_file_src = os.path.join(dir_path, file_name_src)
                path_file_dest = os.path.join(path_dest, file_name_src)                
                os.replace(path_file_src, path_file_dest)      

# Домашнее задание 1
# Функция группового переименования файлов
# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. 
# Она должна: a. принимать параметр желаемое конечное имя файлов desired_name. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере num_digits.
# c. принимать параметр расширение исходного файла source_ext . Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла target_ext.
# e. принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории.

# Пример использования.
# На входе:
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

# На выходе:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", saved_part_indexes=[0, -1]):  
    # Создать тестовую папку
    # folder_name = "test_folder"
    # folder_path = os.path.join(os.getcwd(), folder_name)
    # if os.path.exists(folder_path):
    #     shutil.rmtree(folder_path)
    # os.makedirs(folder_path)
    
    # Заполнить тестовую папку тест 1
    # file_name = "test1.txt"
    # file_path = os.path.join(folder_path, file_name)
    # with open(file_path, "w") as file:
    #     file.write("This is a test file.\n")
    #     file.close()

    # Заполнить тестовую папку тест 3
    # for i in range(10):
    #     file_name = f"test{i}.txt"
    #     file_path = os.path.join(folder_path, file_name)
    #     with open(file_path, "w") as file:
    #         file.write("This is a test file.\n")
    #         file.close()
    # file_name = "test.doc"
    # file_path = os.path.join(folder_path, file_name)
    # with open(file_path, "w") as file:
    #     file.write("This is a test file.\n")
    #     file.close()

    current_path = os.path.join(os.getcwd(), 'test_folder')      
    files_names_src = [file for file in os.listdir(current_path) if os.path.isfile(os.path.join(current_path, file))]      
    files_count = 0
    for file_name_src in files_names_src:  
        file_name_without_ext, *ext_src = file_name_src.split('.')        
        if len(ext_src) and ext_src[0] == source_ext:        
            files_count += 1
            saved_part_of_file_name = file_name_without_ext[saved_part_indexes[0]:saved_part_indexes[1] + 1]
            file_name_dest = f'{saved_part_of_file_name}{desired_name}{files_count:0>{num_digits}}.{target_ext}'                                        
            path_file_src = os.path.join(current_path, file_name_src)
            path_file_dest = os.path.join(current_path, file_name_dest)            
            os.rename(path_file_src, path_file_dest)
        
    # files = os.listdir(folder_path)
    # files.sort()
    # separator = ", "
    # files_as_string = separator.join(files)
    # print(files_as_string)

    # shutil.rmtree(folder_path)


if __name__ == '__main__':
    # 1
    #file_fill_int_float('seminar14/seminar_14_1.txt', 10)

    # 2
    #file_generate_pseudonyms('seminar14/seminar_14_2.txt', 30)

    # 3
    #file_multiply_and_rename('seminar14/seminar_14_3.txt', 'seminar14/seminar_14_1.txt', 'seminar14/seminar_14_2.txt')

    # 4, 6
    #file_create_files_with_ext('ver1', 'seminar14files')

    # 5, 6
    #file_create_files_with_several_ext({'avi':5, 'mp4':4, 'txt':4, 'doc':2, 'jpg':2, 'bmp':3, 'dat':5}, 'seminar14files')

    # 7    
    #file_sort_files_by_dirs({'avi':'video', 'mp4':'video', 'txt':'docs', 'doc':'docs', 'jpg':'images', 'bmp':'images'}, 'seminar14files')

    # ДЗ 1
    # тест 1
    #rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")    
    # тест 3
    #rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")    
    pass

# решение автотеста (на мой взгляд, неудачное в плане формирования первоначальной выборки)
# import os

# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []

#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')

#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]

#     # Сортируем файлы по имени
#     filtered_files.sort()

#     # Задаем начальный номер для порядкового номера
#     num = 1

#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]

#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]

#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)

#         # Увеличиваем порядковый номер
#         num += 1

