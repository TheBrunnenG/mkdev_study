class Figure:
    def color(self, color):
        self.color = color


class Square(Figure):
    def side(self, side):
        self.side = side


class Circle(Figure):
    def radius(self, radius):
        self.radius = radius


class Triangle(Figure):
    def side(self, side):
        self.side = side

