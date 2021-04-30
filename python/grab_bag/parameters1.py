# @desc Default values can be specified for parameters!

def add_it(x, y=5):
    answer = x + y
    return answer


def main():
    print(add_it(2, 6))
    print(add_it(8))
    print(add_it(-5, 4))
    print(add_it(-2))
    print(add_it(0))


if __name__ == '__main__':
    main()
