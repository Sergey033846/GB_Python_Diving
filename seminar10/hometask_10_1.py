# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#
# Пример использования:
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
#
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

# мое решение
def get_file_info(*, file_path: str):
    *path, name = file_path.split('/')
    path = f"{'/'.join(path)}/" if len(path) > 0 else ""
    if '.' in name:
        *name, ext = str(name).split('.')
        name = '.'.join(name)
    else:
        ext = ''
    ext = f'.{ext}' if len(ext) > 0 else ''
    return path, name, ext


# решение автотеста (по значениям file_path0 и file_path1 некорректное)
# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)


file_path0 = 'C:/Users/User/Documents/'
file_path1 = 'C:/Users/User/Documents/exampletxt'
file_path2 = 'C:/Users/User/Documents/example.txt'
file_path3 = '/home/user/data/file.py'
file_path4 = 'D:/myfile.txt'
file_path5 = 'C:/Projects/project1/code/script.py'
file_path6 = '/home/user/docs/my.file.with.dots.txt'
file_path7 = 'file_in_current_directory.txt'

print(get_file_info(file_path=file_path0))
print(get_file_info(file_path=file_path1))
print(get_file_info(file_path=file_path2))
print(get_file_info(file_path=file_path3))
print(get_file_info(file_path=file_path4))
print(get_file_info(file_path=file_path5))
print(get_file_info(file_path=file_path6))
print(get_file_info(file_path=file_path7))
