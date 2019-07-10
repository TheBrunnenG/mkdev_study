# класс Figure с атрибутами color и side, принимающих параметры цвета и размера стороны (радиуса) геометрических фигур
class Figure:
    def __init__(self, color, side):
        self.color = color
        self.side = side


# создаем три класса Square, Circle и Triangle, которые будут наследовать атрибуты родительского класса Figure
class Square(Figure):
    pass


class Circle(Figure):
    pass


class Triangle(Figure):
    pass


# создадим три фигуры из классов Square, Circle и Figure
first_figure = Square("red", 20)
second_figure = Circle("orange", 15)
third_figure = Triangle("yellow", 30)

# выведем информацию о фигурах и их атрибутах
print("First figure is", first_figure.color, type(first_figure).__name__, "with side", first_figure.side)
print("Second figure is", second_figure.color, type(second_figure).__name__, "with radius", second_figure.side)
print("Third figure is", third_figure.color, type(third_figure).__name__, "with side", third_figure.side)
