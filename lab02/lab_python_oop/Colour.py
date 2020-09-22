class Colour():
    def __init__(self,colour=''):
        self._colour=colour
    @property
    def colour(self):
        return self.colour
    @colour.setter
    def colour(self, value):
        self._colour=value
    @colour.deleter
    def colour(self):
        del self._colour
