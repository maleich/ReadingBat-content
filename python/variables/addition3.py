# @desc Determine the value returned by the function.

def adder(val1, val2):
    total = val1 + val2
    return total


def main():
    print(adder(2, 3))
    print(adder(2, -2))
    print(adder(0, 20))
    print(adder(-50, 15))
    print(adder(6, 5))


if __name__ == '__main__':
    main()
