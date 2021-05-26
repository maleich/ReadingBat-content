# @desc Determining a number's divisibility
# @desc by Savonnah '23

def divisibilty_name(num):
    result = num % 3
    if result == 0:
        return True
    else:
        return False


def main():
    print(divisibilty_name(3))
    print(divisibilty_name(56))
    print(divisibilty_name(6))
    print(divisibilty_name(61))


if __name__ == '__main__':
    main()