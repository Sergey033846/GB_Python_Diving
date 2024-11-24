# Задание №1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. 
# 📌 Имена пишите с большой буквы. 
# 📌 Каждую пару сохраняйте с новой строки.


import json


def file_multiply_and_rename_2_json(file_src_txt, file_dest_json): 
    with (
        open(file_src_txt, 'r', encoding='utf-8') as ftxt,
        open(file_dest_json, 'w', encoding='utf-8') as fjson
        ):
        for line in ftxt:
            key, value = line.replace('\n', '').split(',')            
            print(json.dumps({key.title(): value}), file=fjson)
                        

file_multiply_and_rename_2_json('seminar16/seminar_16_1.txt', 'seminar16/seminar_16_1.json')
