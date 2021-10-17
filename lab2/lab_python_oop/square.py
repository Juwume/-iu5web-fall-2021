from lab_python_oop import rectangle


class Square(rectangle.Rectangle):
    name = 'Квадрат'

    def __init__(self, side, color) -> None:
        super().__init__(side, side, color)

    def repr(self):
        return '{} со стороной: {} и цветом {}'.format(self.name, self._height, self._color.rgb)
