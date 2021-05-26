# determining a number's divisibility by 3

def divisibilty_name(num):     # from number that is tested, it will determine if it is divisible by 3
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