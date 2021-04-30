# @desc Determine the value returned by the function.

def product(x, y):
    result = x * y
    return result


def main():
    print(product(2, 3))
    print(product(-2, 1))
    print(product(-1, -2))
    print(product(5, 3))


if __name__ == '__main__':
    main()
