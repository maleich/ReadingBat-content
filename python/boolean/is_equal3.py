# @desc What is returned?
# @desc by Savonnah '23

def equal(num1, num2, num3):
    result = num1 == num2 == num3
    return result

def main():
    print(equal(3,4,7))
    print(equal(5,5,5))
    print(equal(6,7,9))
    print(equal(4,7,4))


if __name__ == '__main__':
    main()
