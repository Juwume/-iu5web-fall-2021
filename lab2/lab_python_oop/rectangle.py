from lab_python_oop import geometric_figure
from lab_python_oop import fig_color


class Rectangle(geometric_figure.GeometricFigure):
    name = 'Прямоугольник'

    def __init__(self, width, height, color) -> None:
        self._width = float(width)
        self._height = float(height)
        self._color = fig_color.Color(color)

    def square(self):
        return self._width * self._height

    def repr(self):
        return '{} с шириной: {}, высотой: {} и цветом {}'.format(self.name, self._width, self._height, self._color.rgb)
