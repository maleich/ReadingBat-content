# @desc Pay close attention to details such as indentations!

def practice(i):
    while i < 6:
        if i == 3:
            break
        i += 1
    return i


def main():
    print(practice(10))
    print(practice(3))
    print(practice(-2))
    print(practice(1))
    print(practice(6))


if __name__ == '__main__':
    main()
