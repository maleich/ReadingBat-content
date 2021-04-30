# @desc Determine the value returned by the function. Pay close attention to variable types!

def add_num(num):
    total = num + 2.5
    return total


def main():
    print(add_num(2.25))
    print(add_num(-2))
    print(add_num(10))
    print(add_num(-2.75))


if __name__ == '__main__':
    main()
