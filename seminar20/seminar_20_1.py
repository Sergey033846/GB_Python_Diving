# Задание №1
# 📌 Создайте класс окружность. 
# 📌 Класс должен принимать радиус окружности при создании экземпляра. 
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.


from math import pi


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def length(self):
        return 2 * pi * self.radius
    
    def area(self):
        return pi * self.radius * self.radius
    


if __name__ == '__main__':
    circle = Circle(5)
    print(f'{circle.length() = }')
    print(f'{circle.area() = }')
