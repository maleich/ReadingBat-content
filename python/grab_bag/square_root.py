# @desc Predict the result
# @desc by Yuk '24
# @desc (Note: assume the math module is already imported)

import math
def square_roots(n):
    if math.sqrt(n) == (n / 2) and n >= 0:
        return True
    else:
        return False


def main():
    print(square_roots(4))
    print(square_roots(1))
    print(square_roots(9))
    print(square_roots(36))
    print(square_roots(16))


if __name__ == '__main__':
    main()
