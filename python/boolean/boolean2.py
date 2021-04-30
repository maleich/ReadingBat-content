# @desc Evaluate the overengineered XOR gate. By Benji '24

def XOR(bool1, bool2):
    value1 = bool1 or bool2
    value2 = not (bool1 and bool2)
    return value1 and value2


def main():
    print(XOR(False, False))
    print(XOR(False, True))
    print(XOR(True, False))
    print(XOR(True, True))


if __name__ == '__main__':
    main()
