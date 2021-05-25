# @desc Determine if a is greater that 0
# @desc by Tracy '23

def true_or_false(a):
    if a > 0:
        return True
    else:
        return False

def main():
    print(true_or_false(5 / 4))
    print(true_or_false(-1 + 2))
    print(true_or_false(0 * -1))
    print(true_or_false(6 - 10))


if __name__ == '__main__':
    main()
