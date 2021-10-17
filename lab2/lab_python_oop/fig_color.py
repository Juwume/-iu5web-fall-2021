class Color:

    def __init__(self, value):
        """RGB color class"""
        self._color = tuple(value)

    @property
    def rgb(self):
        return self._color

    @rgb.setter
    def rgb(self, value):
        self._color = tuple(value)
