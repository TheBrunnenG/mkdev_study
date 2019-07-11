# импортируем число Пи и расчет корня из библиотеки math
from math import pi, sqrt


# класс Figure с атрибутами color и side принимает параметры цвета и размера стороны (радиуса) геометрических фигур
class Figure:
    def __init__(self, color, side):
        self.color = color
        self.side = side


# классы Square, Circle и Triangle наследуют атрибуты родительского класса Figure и считают площадь встроенными методами
class Square(Figure):
    def square(self, side):
        return side ** 2
    @property
    def description(self):
        return (self.color, self.side)
    @staticmethod
    def perimeter(side):
        return 4 * side


class Circle(Figure):
    def square(self, side):
        return pi * side ** 2
    @property
    def description(self):
        return (self.color, self.side)
    @staticmethod
    def perimeter(side):
        return 2 * pi * side


class Triangle(Figure):
    def square(self, side):
        return sqrt(3) / 4 * side ** 2
    @property
    def description(self):
        return (self.color, self.side)
    @staticmethod
    def perimeter(side):
        return 3 * side


# создадим три фигуры из классов Square, Circle и Figure
first_figure = Square("red", 20)
second_figure = Circle("orange", 15)
third_figure = Triangle("yellow", 30)

# выведем информацию о фигурах и их атрибутах
print("First figure, parameters (color, side):", first_figure.description)
print("First figure, perimeter:", first_figure.perimeter(first_figure.side))
print("Second figure, parameters (color, side):", second_figure.description)
print("Second figure, perimeter:", second_figure.perimeter(second_figure.side))
print("Third figure, parameters (color, side)", third_figure.description)
print("Third figure, perimeter:", third_figure.perimeter(third_figure.side))

# вывод площади фигур через методы, встроенные в классы каждой фигуры
print(first_figure.square(side=first_figure.side))
print(second_figure.square(side=second_figure.side))
print(third_figure.square(side=third_figure.side))
