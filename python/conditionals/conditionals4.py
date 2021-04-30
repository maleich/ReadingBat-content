# @desc Predict the result... By Margot '24

def calc(x):
    if x % 7 == 0:
        return x + 100
    else:
        return x


def main():
    print(calc(17))
    print(calc(49))
    print(calc(84))
    print(calc(62))


if __name__ == '__main__':
    main()
