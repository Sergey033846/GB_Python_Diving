# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). 
# 📌 После каждого ввода добавляйте новую информацию в JSON файл. 
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени. 
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.


import json


def creating_access_database(file_json): 
    access_dict = dict()
        
    # читаем предыдущий словарь доступа из файла
    with open(file_json, 'r', encoding='utf-8') as fjson:
        access_dict = json.load(fjson)
    print(f'Текущая база данных доступа:\n{access_dict=}\n')    
    
    # вводим и добавляем сначала в словарь, затем в файл
    while True:
        inputstr = input('Введите через пробел имя, личный id и уровень доступа от 1 до 7 ("q" для выхода): ')
        if inputstr == 'q':
            break
        else:
            name, user_id, access_level = inputstr.split()
            if 1 <= int(access_level) <= 7:  
                if not any(user_id in dict_level for dict_level in access_dict.values()):
                    if access_level in access_dict:
                        access_dict[access_level][user_id] = name
                    else:                
                        access_dict[access_level] = {user_id: name}
                    
                    with open(file_json, 'w', encoding='utf-8') as fjson:                
                        json.dump(access_dict, fjson, indent=2)
                else:
                    print('Такой user_id уже существует!')
            else:
                print('Указан недопустимый уровень доступа (1-7)!')
    
    print(f'Новая база данных доступа:\n{access_dict=}\n')


creating_access_database('seminar16/accessdb.json')
