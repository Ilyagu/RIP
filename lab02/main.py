from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


def main():
    r = Rectangle(12, 12,"синего")
    c = Circle(12,"зеленого")
    s = Square(12,"красного")
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()