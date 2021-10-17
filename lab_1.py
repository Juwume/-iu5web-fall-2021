import argparse
import sys
import math


def parse_func(args):
    parser = argparse.ArgumentParser(description='parser for equality coefs')
    parser.add_argument('-A', action='store', dest='A', help='"A" coef')
    parser.add_argument('-B', action='store', dest='B', help='"B" coef')
    parser.add_argument('-C', action='store', dest='C', help='"C" coef')

    return parser.parse_args(args)


def main():
    params = parse_func(sys.argv[1:])
    A = params.A
    B = params.B
    C = params.C
    while A is None or B is None or C is None:
        print("Input all coefs(A, B, C): ")
        A, B, C = tuple(map(float, (input().strip().split(','))))
    discr = B**2 - 4*A*C
    if discr < 0:
        print('No real roots')
    elif round(discr, 6) == 0:   # Считаем с точностью в 6 знаков
        print('There is one real root: ' + str(-B/(2*A)))
    else:
        print('There is two real roots: ' + str((-B+math.sqrt(discr)) /
              (2*A)) + ' and ' + str((-B-math.sqrt(discr)) / (2*A)))


if __name__ == '__main__':
    main()
