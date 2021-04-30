# @desc Checking to see if a number is less than another number

def less_than(num):
    x = (num < 5)
    return x


def main():
    print(less_than(3))
    print(less_than(5))
    print(less_than(7))


if __name__ == '__main__':
    main()
