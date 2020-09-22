from lab_python_oop.figure import Figure
from lab_python_oop.Colour import Colour
from math import pi

class Circle(Figure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius=0,colour=''):
        self._radius=radius
        self.col_par=Colour()
        self.col_par.colour=colour

    def area(self):
        return self._radius*self._radius*pi

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.col_par._colour,
            self._radius,
            self.area()
        )