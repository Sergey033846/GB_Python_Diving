import csv
import json
import pickle
import os


__all__ = ['get_dir_size', 'traverse_directory', 'save_results_to_csv', 'save_results_to_json', 'save_results_to_pickle']


# Домашнее задание 1
# Задача по обходу и анализу файловой системы
# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории. 
# Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:
# - Путь к файлу или директории: Абсолютный путь к файлу или директории. 
# - Тип объекта: Это файл или директория. 
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. 

# Важные детали:
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Для файлов сохраните их размер в байтах.
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.

# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

# Для обхода файловой системы вы можете использовать модуль os.
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать результаты в виде списка словарей. 
# После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) 
# с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

# Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий. 
# При этом сначала добавляются файлы, а затем директории.

# Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)), 
# и затем получается размер файла (size = os.path.getsize(path)). 
# Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.

# Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)), 
# и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого. 
# Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.


def get_dir_size(root):
    dir_size = 0
    for dir_path, _, ﬁles in os.walk(root):        
        for file in files:
            path = os.path.join(dir_path, file)
            size = os.path.getsize(path)            
            dir_size += size            
    return dir_size


def traverse_directory(root):      
    results = []
    for dir_path, dirs, ﬁles in os.walk(root):                     
        for file in files:
            path = os.path.join(dir_path, file)
            size = os.path.getsize(path)                        
            results.append({'Path': path, 'Type': 'File', 'Size': size})    
        for dir in dirs:            
            path = os.path.join(dir_path, dir)
            size = get_dir_size(path)                        
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})    
    return results
    

def save_results_to_json(src_list_of_dict, file_name_dest):
    with open(file_name_dest, 'w', encoding='utf-8') as fjson:        
        json.dump(src_list_of_dict, fjson)
                       

def save_results_to_csv(src_list_of_dict, file_name_dest):
    with open(file_name_dest, 'w', newline='', encoding='utf-8') as fcsv:        
        csv_write = csv.DictWriter(fcsv, fieldnames=['Path', 'Type' ,'Size'], quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(src_list_of_dict)        
                

def save_results_to_pickle(src_list_of_dict, file_name_dest):    
    with open(file_name_dest, 'wb') as fpickle:        
        pickle.dump(src_list_of_dict, fpickle)
                    

if __name__ == '__main__':
    #print(traverse_directory(os.path.join(os.getcwd(), '_testdir')))
    #print(traverse_directory('geekbrains/my_ds_projects'))
    #print(traverse_directory('geekbrains'))

    file_dir_info_dict = traverse_directory('_testdir')
    print(file_dir_info_dict)
    save_results_to_json(file_dir_info_dict,'seminar16/hometask_16_1.json')    
    save_results_to_csv(file_dir_info_dict,'seminar16/hometask_16_1.csv')
    save_results_to_pickle(file_dir_info_dict,'seminar16/hometask_16_1.pkl')
    # with open('seminar16/hometask_16.pkl', 'rb') as f:
    #     data = pickle.load(f)
    # print(data)


# решение автотеста
# import os
# import json
# import csv
# import pickle

# def get_dir_size(directory):
#     total_size = 0

#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             total_size += os.path.getsize(path)

#     return total_size

# def traverse_directory(directory):
#     results = []

#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             size = os.path.getsize(path)
#             results.append({'Path': path, 'Type': 'File', 'Size': size})

#         for name in dirs:
#             path = os.path.join(root, name)
#             size = get_dir_size(path)
#             results.append({'Path': path, 'Type': 'Directory', 'Size': size})

#     return results

# def save_results_to_json(results, file_path):
#     with open(file_path, 'w') as file:
#         json.dump(results, file)

# def save_results_to_csv(results, file_path):
#     with open(file_path, 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
#         writer.writeheader()
#         writer.writerows(results)

# def save_results_to_pickle(results, file_path):
#     with open(file_path, 'wb') as file:
#         pickle.dump(results, file)
