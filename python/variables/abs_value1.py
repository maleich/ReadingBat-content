# @desc Determine the value returned by the function.

def abs_value(num):
    result = abs(num)
    return result


def main():
    print(abs_value(2))
    print(abs_value(-105))
    print(abs_value(-50))
    print(abs_value(3))


if __name__ == '__main__':
    main()
