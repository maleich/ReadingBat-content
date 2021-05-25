# @desc Predict the returned value
# @desc by Tracy '23
def return_to_a_value(x):
    list = ['apple','banana','orange','pineapple','kiwi','grapes','strawberry']
    return list[x]


def main():
    print(return_to_a_value(2))
    print(return_to_a_value(3))
    print(return_to_a_value(5 - 5))
    print(return_to_a_value(1 + 5))


if __name__ == '__main__':
    main()