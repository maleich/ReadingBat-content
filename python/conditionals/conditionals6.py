# @desc Determine the value returned by the function.
# @desc by Bernie '21

def is_percent(x):
    if type(x) == float or type(x) == int:
        if x <= 100 and x >= 0:
            return str(x)
        elif x > 100:
            return "Too high"
        else:
            return "Too low"
    else:
        return "Invalid"


def main():
    print(is_percent(2.5))
    print(is_percent("Water"))
    print(is_percent(107))
    print(is_percent(-12))
    print(is_percent(90))

if __name__ == '__main__':
    main()