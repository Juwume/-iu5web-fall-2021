from lab_python_oop import geometric_figure
from lab_python_oop import fig_color
import math


class Circle(geometric_figure.GeometricFigure):

    name = 'Круг'

    def __init__(self, radius, color) -> None:
        self._radius = float(radius)
        self._color = fig_color.Color(color)

    def square(self):
        return math.pi * self._radius**2

    def repr(self):
        return '{} с радиусом: {} и цветом {}'.format(self.name, self._radius, self._color.rgb)
