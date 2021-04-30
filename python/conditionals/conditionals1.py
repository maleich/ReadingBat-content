# @desc By Anay '24

def check_age(age):
    if age < 21:
        return age

    return age + 5


def main():
    print(check_age(5))
    print(check_age(29))
    print(check_age(42))
    print(check_age(15))
    print(check_age(0.38))
    print(check_age(21))


if __name__ == '__main__':
    main()
