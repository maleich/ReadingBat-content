# @desc This is a code that determines whether a number is positive, negative, or just 0
# @desc by Merrick '23

def positive_negative(x):
    if x > 0:
        return "pos"
    elif x == 0:
        return "0"
    else:
        return "neg"


def main():
    print(positive_negative(5))
    print(positive_negative(-1))
    print(positive_negative(0))
    print(positive_negative(21))
    print(positive_negative(-100))


if __name__ == '__main__':
    main()
