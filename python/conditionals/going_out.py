# @desc In this exercise, you will need to figure out whether or not you are going out or not.
# @desc by Zara '24

def going_out(rain, friends):
    rain = "no"
    friends = "no"
    if rain == "yes":
        if friends == "yes":
            return friends, 'you can go out'
        else:
            return rain, 'you cannot go out'
    else:
        return friends, 'you can go out'


def main():
    print(going_out("yes", "yes"))
    print(going_out("yes", "no"))
    print(going_out("no", "no"))
    print(going_out("no", "yes"))


if __name__ == '__main__':
    main()
