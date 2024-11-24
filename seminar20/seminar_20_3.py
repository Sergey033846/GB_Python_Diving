# Задание №3
# 📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# 📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


class Person:
    def __init__(self, lastname, firstname, middlename, age) -> None:
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.__age = age
    
    def birthday(self):
        self.__age += 1
        return self.__age
    
    def full_name(self):
        result = f'{self.lastname} {self.firstname} {self.middlename}'        
        return result
    


if __name__ == '__main__':
    person1 = Person('Иванов', 'Иван', 'Иванович', 23)    
    print(f'{person1.full_name() = }')
    print(f'{person1.birthday() = }')       # 24
        
    person1.__age = 54
    print(f'{person1.__age = }')            # 54
    print(f'{person1.birthday() = }')       # 25    
    