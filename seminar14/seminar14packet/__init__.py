# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него функцию rename_files

import os
import shutil
import my_files

__all__ = ['rename_files']

def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", saved_part_indexes=[0, -1]):  
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
