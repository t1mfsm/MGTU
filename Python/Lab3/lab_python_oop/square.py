from lab_python_oop.rectangle import Rectangle
class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"
    def __init__(self, a, color):
        self.a = a
        super().__init__(self.a, self.a, color)

    def __repr__(self):
        return '{} {} цвета со стороной {}, площадью {}.'.format(
            self.FIGURE_TYPE,
            self.r_color._color,
            self.a,
            self.area()
        )