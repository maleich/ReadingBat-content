# @desc Determine the value returned by the function.

def round_it(num, places):
    rounded = round(num, places)
    return rounded


def main():
    print(round_it(2.562, 1))
    print(round_it(45.3327, 2))
    print(round_it(-16.255, 1))
    print(round_it(6.5539, 3))


if __name__ == '__main__':
    main()
