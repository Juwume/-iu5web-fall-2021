# Здесь должна быть реализация декоратора
def print_result(func):
    def wrapper():

        out = func()
        print(func.__name__)
        if isinstance(out, list):
            for val in out:
                print(val)
        elif isinstance(out, dict):
            for key, val in out.items():
                print('{} = {}'.format(key, val))
        else:
            print(out)

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
