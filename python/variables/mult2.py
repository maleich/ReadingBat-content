# @desc Determine the value returned by the function. Pay close attention to data types!

def product(x, y):
    result = x * y
    return result


def main():
    print(product('cat', 2))
    print(product('3', 4))
    print(product('-1', 3))
    print(product('53', 3))


if __name__ == '__main__':
    main()
