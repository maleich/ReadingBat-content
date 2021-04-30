# @desc Reading while loops

def countup(n):
    total = 0
    while n < 5:
        total = total + n
        n += 1
    return total


def main():
    print(countup(0))
    print(countup(3))
    print(countup(-2))


if __name__ == '__main__':
    main()
