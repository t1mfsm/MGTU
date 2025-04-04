from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.r_color = Color(color)

    def area(self):
        return self.a * self.b

    def __repr__(self):
       return '{} {} цвета шириной {} и высотой {}, площадью {}.'.format(
            self.FIGURE_TYPE,
            self.r_color._color,
            self.a,
            self.b,
            self.area()
        )