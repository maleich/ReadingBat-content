# @desc Even or odd?
# @desc Yuk '24

def odd_even(n):
    if n < 100:
        return n % 2 == 0
    else:
        return n % 2 != 0


def main():
    print(odd_even(5))
    print(odd_even(22))
    print(odd_even(122))
    print(odd_even(75))
    print(odd_even(98))
    print(odd_even(1001))


if __name__ == '__main__':
    main()
