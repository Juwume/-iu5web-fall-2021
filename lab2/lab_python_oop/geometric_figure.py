from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    @abstractmethod
    def square(self):
        pass

    def repr(self):
        pass
