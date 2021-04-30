# @desc Determine the value returned by the function.

def add_5(num):
    total = num + 5
    return total


def main():
    print(add_5(2))
    print(add_5(0))
    print(add_5(-50))
    print(add_5(-3))


if __name__ == '__main__':
    main()
