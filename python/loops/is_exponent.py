# @desc Determine the value returned by the function.
# @desc by Bernie '21

def power_find(x,y):
    x_1 = x
    i = 1
    while x < y:
        x *= x_1
        i += 1
    if x == y:
        result=f"{x_1} to the power of {i} is {y}"
    else:
        result="X is not an exponential of Y"
    return result


def main():
    print(power_find(2,8))
    print(power_find(4,64))
    print(power_find(3,71))
    print(power_find(6,20))


if __name__ == '__main__':
    main()