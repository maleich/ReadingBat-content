# @desc Checking to see if a number is not equal to another number

def not_equal(num):
    x = (num != 5)
    return x


def main():
    print(not_equal(3))
    print(not_equal(5))
    print(not_equal(7))


if __name__ == '__main__':
    main()
