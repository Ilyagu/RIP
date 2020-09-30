from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
from colorama import Back,Fore,Style

def main():
    r = Rectangle(12, 12,"синего")
    c = Circle(12,"зелёного")
    s = Square(12,"красного")
    print(Back.BLUE)
    print(r)
    print(Back.GREEN)
    print(c)
    print(Back.RED)
    print(s)

if __name__ == "__main__":
    main()