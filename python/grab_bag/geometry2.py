# @desc Enter a number to find the perimeter of a square with a side length of the value you entered.
#  @desc Negative values will not be accepted.
# @desc by Alex '24

def times_4(side):
    invalid = -1
    perim = side * 4
    while perim == side * 4:
        if perim >= 0:
            return perim
        else:
            return invalid


def main():
    print(times_4(2))
    print(times_4(0))
    print(times_4(-50))
    print(times_4(-3))
    print(times_4(12))


if __name__ == '__main__':
    main()
