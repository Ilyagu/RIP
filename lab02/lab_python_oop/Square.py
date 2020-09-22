from .Rectangle import Rectangle

class Square(Rectangle):

    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self,side=0,colour=''):
        self.side = side
        super().__init__(self.side, self.side, colour)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.col_par.colour,
            self.side,
            self.area()
        )

