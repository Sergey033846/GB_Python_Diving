# Задание №2
# 📌 Создайте класс прямоугольник. 
# 📌 Класс должен принимать длину и ширину при создании экземпляра. 
# 📌 У класса должно быть два метода, возвращающие периметр и площадь. 
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, *args) -> None:
        self.a = args[0]
        self.b = args[1] if len(args) > 1 else self.a
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b
    


if __name__ == '__main__':
    rectangle = Rectangle(5, 4)
    print(f'{rectangle.perimeter() = }')
    print(f'{rectangle.area() = }')
