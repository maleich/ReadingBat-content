# @desc Determine the value returned by the function.

def diff(num1, num2):
    total = num1 + num2
    return total


def main():
    print(diff(5, 2))
    print(diff(5, 8))
    print(diff(12, 6))
    print(diff(5, 5))


if __name__ == '__main__':
    main()
