# @desc Determine the value returned by the function.

def exp(x, y):
    result = x ** y
    return result


def main():
    print(exp(2, 3))
    print(exp(5, 1))
    print(exp(20, 0))
    print(exp(6, 2))


if __name__ == '__main__':
    main()
