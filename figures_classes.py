class Figure:
    def __init__(self, color, side):
        self.color = color
        self.side = side


class Square(Figure):
    pass


class Circle(Figure):
    pass


class Triangle(Figure):
    pass


first_figure = Square("red", 20)
second_figure = Circle("orange", 15)
third_figure = Triangle("yellow", 30)

print("First figure is", first_figure.color, type(first_figure).__name__, "with side", first_figure.side)
print("Second figure is", second_figure.color, type(second_figure).__name__, "with radius", second_figure.side)
print("Third figure is", third_figure.color, type(third_figure).__name__, "with side", third_figure.side)
