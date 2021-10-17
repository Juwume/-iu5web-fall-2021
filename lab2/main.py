from lab_python_oop import square
from lab_python_oop import circle
from lab_python_oop import rectangle
import requests


def main():
    ex1 = square.Square(12, (0, 255, 0))
    ex2 = circle.Circle(12, (255, 0, 0))
    ex3 = rectangle.Rectangle(12, 12, (0, 0, 255))
    print(ex1.repr())
    print(ex2.repr())
    print(ex3.repr())
    print(requests.get('http://yandex.ru'))


if __name__ == '__main__':
    main()
