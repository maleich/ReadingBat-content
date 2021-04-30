# @desc Predict the output
# @desc by Sam '24

def math(num):
    step1 = num + (num / 2)
    step2 = step1 + 3
    step3 = step2 * 3
    return step3


def main():
    print(math(2))
    print(math(6))
    print(math(10))
    print(math(30))


if __name__ == '__main__':
    main()
