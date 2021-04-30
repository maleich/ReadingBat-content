# @desc Checking to see if a number is greater than another number
def greater_than(num):
    x = (num > 5)
    return x


def main():
    print(greater_than(3))
    print(greater_than(5))
    print(greater_than(7))


if __name__ == '__main__':
    main()
