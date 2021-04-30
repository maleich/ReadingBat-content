# @desc Predict the returned result
# by Bruno '24

def adding(x, y):
    new_list = 0
    for char in range(0, x):
        new_list += y
    return new_list


def main():
    print(adding(5, 3))
    print(adding(10, 4))
    print(adding(15, 2))
    print(adding(20, 1))


if __name__ == '__main__':
    main()
