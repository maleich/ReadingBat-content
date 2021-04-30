# @desc Determine the value returned by the function.

def mod(x, y):
    result = x % y
    return result


def main():
    print(mod(2, 2))
    print(mod(5, 4))
    print(mod(20, 7))
    print(mod(6, 3))
    print(mod(3, 5))
    print(mod(22, 9))
    print(mod(5, 2))


if __name__ == '__main__':
    main()
