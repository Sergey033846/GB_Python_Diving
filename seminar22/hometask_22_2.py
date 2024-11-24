# ДЗ 2
# Класс Archive - архив текстовых и числовых записей
# Разработайте программу для хранения и управления текстовыми и числовыми записями.
# Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:

# Методы и операции:
# При создании экземпляра класса Archive с указанием текстовой и числовой записи (text и number)
# записи добавляются в соответствующие атрибуты archive_text и archive_number. 
# Если архив уже существует, текущие записи (text и number) добавляются в архив.

# Метод __str__ возвращает строковое представление объекта, включая текущие записи (text и number) и архивированные записи (archive_text и archive_number).
# Метод __repr__возвращает строковое представление объекта, которое можно использовать для создания нового объекта того же класса с теми же записями.
# Архивированные записи могут быть получены через атрибуты archive_text и archive_number.
# Метод __new__ - это статический метод, который создает новый экземпляр класса. 
# Первым аргументом метод __new__ получает ссылку на класс (cls), а затем может принимать дополнительные аргументы. 
# Метод __new__ проверяет, существует ли уже экземпляр класса Archive (с использованием атрибута _instance). 
# Если экземпляр существует, то метод вместо создания нового экземпляра добавляет текущие значения text и number в архив 
# (списки archive_text и archive_number) для уже существующего экземпляра. 
# Если экземпляр еще не существует, метод создает новый экземпляр класса Archive с пустыми архивами для текстовых и числовых записей. 
# В любом случае метод возвращает созданный или существующий экземпляр класса Archive.

# Метод __init__ - это конструктор экземпляра класса, который вызывается после создания экземпляра с использованием метода __new__. 
# Метод __init__ принимает два аргумента: text (строка) и number (целое число или число с плавающей точкой). 
# В методе __init__устанавливаются атрибуты text и number текущего экземпляра класса для хранения переданных текстовой и числовой записей. 
# Эти записи могут быть затем добавлены в архив (списки archive_text и archive_number) с использованием метода __new__.

# Пример

# На входе:
# archive1 = Archive("Запись 1", 42)
# archive2 = Archive("Запись 2", 3.14)

# На выходе:
# Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]
# Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]


class Archive:
    _instance = None
    archive_text = []
    archive_number = []

    def __new__(cls, text, number):
        if not cls._instance:
            cls._instance = super().__new__(cls)      
                    
        cls.archive_text.append(text)
        cls.archive_number.append(number)

        return cls._instance        

    def __init__(self, text, number) -> None:
        self.text = text
        self.number = number
        
    def __str__(self) -> str:                
        return f"Text is {self.text} and number is {self.number}. Also {Archive.archive_text} and {Archive.archive_number}"        
    
    def __repr__(self) -> str:
        return f"Archive('{self.text}', '{self.number}')"



if __name__ == '__main__':
    archive1 = Archive("Запись 1", 42)
    print(archive1)
    print(f'{archive1 = }')
    archive2 = Archive("Запись 2", 3.14)   
    print(archive2)    
    print(f'{archive2 = }')

    

# решение автотеста
# from typing import Union

# class Archive:
#     _instance = None
#     archive_text = []
#     archive_number = []

#     def __new__(cls, text: str, number: Union[int, float]):
#         if cls._instance is None:
#             cls._instance = super(Archive, cls).__new__(cls)
#             cls.archive_text = []
#             cls.archive_number = []
#             return cls._instance
#         return cls._instance

#     def __init__(self, text: str, number: Union[int, float]):
#         self.text = text
#         self.number = number
#         Archive.archive_text.append(self.text)
#         Archive.archive_number.append(self.number)

#     def __repr__(self):
#         return f'Text is {self.text} and number is {self.number}. ' \
#                f'Also {Archive.archive_text} and {Archive.archive_number}'
