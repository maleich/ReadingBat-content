# @desc Determine the value returned by the function.

def f_div(w, z):
    result = w // z
    return result


def main():
    print(f_div(2, 2))
    print(f_div(5, 2))
    print(f_div(20, 3))
    print(f_div(6, 4))
    print(f_div(3, 5))
    print(f_div(22, 3))
    print(f_div(18, 5))


if __name__ == '__main__':
    main()
