import sys
import math
from itertools import groupby

def input_coefficient(prompt):
    while True:
        try:
            coefficient = float(input(prompt))
            return coefficient
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректное числовое значение.")

def get_coefs():
    if len(sys.argv) == 4:
        try:
            a, b, c = map(float, sys.argv[1:])
        except ValueError:
            print("Ошибка: коэффициенты в командной строке заданы некорректно.")
            return
    else:
        a = input_coefficient("Введите коэффициент A: ")
        b = input_coefficient("Введите коэффициент B: ")
        c = input_coefficient("Введите коэффициент C: ")
    return a, b, c

def calculate_roots(a, b, c):
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
    
def print_roots(roots):
    if len(roots) == 0:
        print("Нет действительных корней")
    else:
        roots = list(set(roots))
        print("Действительные корни уравнения:", ', '.join(map(str, roots)))

def main():
    a, b, c = get_coefs()
    roots = calculate_roots(a, b, c)
    print_roots(roots)

if __name__ == "__main__":
    main()
