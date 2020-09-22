from lab_python_oop.figure import Figure
from lab_python_oop.Colour import Colour

class Rectangle(Figure):

    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self,width=0,length=0,colour=''):
        self.width=width
        self.length=length
        self.col_par=Colour()
        self.col_par.colour=colour

    def area(self):
        return self.width*self.length

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.col_par.colour,
            self.width,
            self.length,
            self.area()
        )
