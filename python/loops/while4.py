# @desc Determine the value returned by the function.
# @desc by Bernie '21

def power_find(x, y):
    i = 1
    init_x = x
    while x < y:
        x *= init_x
        i += 1
    if x == y:
        return i
    else:
        return None



def main():
    print(power_find(2,8))
    print(power_find(4,64))
    print(power_find(3,71))
    print(power_find(6,20))


if __name__ == '__main__':
    main()