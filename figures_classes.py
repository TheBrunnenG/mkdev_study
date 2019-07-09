class Figure:
    pass


class Square(Figure):
    def side(self):
        return ("Атрибут стороны квадрата")
    def color(self):
        return ("Атрибут цвета квадрата")


class Circle(Figure):
    def diameter(self):
        return("Атрибут диаметра круга")
    def color(self):
        return ("Атрибут цвета круга")


class Triangle(Figure):
    def side(self):
        return ("Атрибут стороны треугольника")
    def color(self):
        return ("Атрибут цвета треугольника")
