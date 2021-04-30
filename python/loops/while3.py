# @desc What value is returned?

def run_it(x):
    while x > 10:
        if x % 3 == 0:
            return 2
        else:
            x -= 5
    return x


def main():
    print(run_it(10))
    print(run_it(21))
    print(run_it(5))
    print(run_it(25))
    print(run_it(14))


if __name__ == '__main__':
    main()
