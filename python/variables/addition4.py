# @desc Determine the value returned by the function. Pay attention to data types!

def add_str(x, y):
    answer = x + y
    return answer


def main():
    print(add_str('ab', 'cd'))
    print(add_str('3', '2'))
    print(add_str('ca', 't'))
    print(add_str('Athenian', 'Owls'))
    print(add_str('read ', 'books'))
    print(add_str('5', '-5'))


if __name__ == '__main__':
    main()
