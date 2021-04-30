# @desc Check if value is within max_distance units of 0. By Benji '24

def near(value, max_distance):
    if abs(value) <= max_distance:
        return True
    else:
        return False


def main():
    print(near(2, 3))
    print(near(4, 4))
    print(near(7, 3))
    print(near(-2, 4))
    print(near(-6, 5))
    print(near(0, 0))


if __name__ == '__main__':
    main()
