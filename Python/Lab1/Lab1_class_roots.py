import sys
import math
from itertools import groupby

class SquareRoots:

    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.roots = []
    
    def input_coefficient(self, prompt):
        while True:
            try:
                coefficient = float(input(prompt))
                return coefficient
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите корректное числовое значение.")

    def get_coefs(self):
        if len(sys.argv) == 4:
            try:
                self.coef_A, self.coef_B, self.coef_C = map(float, sys.argv[1:])
            except ValueError:
                print("Ошибка: коэффициенты в командной строке заданы некорректно.")
                return
        else:
            self.coef_A = self.input_coefficient("Введите коэффициент A: ")
            self.coef_B = self.input_coefficient("Введите коэффициент B: ")
            self.coef_C = self.input_coefficient("Введите коэффициент C: ")


    def calculate_roots(self):
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        D = b*b - 4*a*c
        f1, f2 = False, False
        x1, x2, x3, x4 = 0, 0, 0, 0
        roots = []
        if D >= 0.0:
            k = math.sqrt(D)
            if -b + k >= 0:
                x1 = math.sqrt((-b + k) / (2*a))
                x2 = -x1
                f1 = True
            if -b - k >= 0:
                x3 = math.sqrt((-b - k) / (2*a))
                x4 = -x3
                f2 = True
            if f1 == True and f2 == True:
                roots.extend([x1, x2, x3, x4])
            elif f1 == True and f2 == False:
                roots.extend([x1, x2])
            elif f1 == False and f2 == True:
                roots.extend([x3, x4])
        return roots

    def print_roots(self):
        self.roots = self.calculate_roots()
        if len(self.roots) == 0:
            print("Нет действительных корней")
        else:
            self.roots = list(set(self.roots))
            print("Действительные корни уравнения:", ', '.join(map(str, self.roots)))
        


def main():
    r = SquareRoots()
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main()