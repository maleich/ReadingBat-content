# @desc Determine the value returned by the function.
# @desc by Bernie '21

def times_tables(x, y):
    result = []
    a = 0
    for i in range(y + 1):
        a = x * i
        result.append(a)
    return result


def main():
    print(times_tables(5, 3))
    print(times_tables(2, 10))
    print(times_tables(3, 3))
    print(times_tables(1, 10))


if __name__ == '__main__':
    main()
