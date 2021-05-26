# @desc Predict the returned value
# @desc by Savonnah '23

def calc(num):
    if num <= 10:
        result = num * 2
    else:
        result = num * 10
    return result

def main():
    print(calc(1))
    print(calc(41))
    print(calc(-5))
    print(calc(3))
    print(calc(10))


if __name__ == '__main__':
    main()