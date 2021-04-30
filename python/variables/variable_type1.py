# @desc Identify the variable type

def what_type(g):
    x = str(type(g))
    if "int" in x:
        return "int"
    elif "str" in x:
        return "str"
    elif "bool" in x:
        return "bool"


def main():
    print(what_type("cat"))
    print(what_type(True))
    print(what_type(7))


if __name__ == '__main__':
    main()
