# @desc Predict the returned value
# @desc by Tracy '23

def plus_or_minus(b):
    if b > 10:
        return b + 2
    if b <= 10:
        return b - 1


def main():
    print(plus_or_minus(8))
    print(plus_or_minus(-12))
    print(plus_or_minus(10))
    print(plus_or_minus(0))
    print(plus_or_minus(15))
    print(plus_or_minus(11))
    print(plus_or_minus(-5))

if __name__ == '__main__':
    main()