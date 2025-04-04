from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
def main():
    r = Rectangle(19, 20, "синего")
    c = Circle(19, "зеленого")
    s = Square(19, "красного")
    print(r)
    print(c)
    print(s)
if __name__ == "__main__":
    main()