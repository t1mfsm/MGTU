from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math
class Circle(Figure):
    FIGURE_TYPE = "Круг"
    def __init__(self, r, color):
        self.r = r
        self.c_color = Color(color)

    def area(self):
       return math.pi * (self.r ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {}, площадью {}.'.format(
            self.FIGURE_TYPE,
            self.c_color._color,
            self.r,
            self.area()
        )