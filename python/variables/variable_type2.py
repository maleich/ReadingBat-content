# @desc Identify the variable type

def what_type(g):
    x = str(type(g))
    if "int" in x:
        return "int"
    elif "str" in x:
        return "str"
    elif "bool" in x:
        return "bool"
    elif "float" in x:
        return "float"


def main():
    print(what_type(3.1415))
    print(what_type(3))
    print(what_type(3.0))
    print(what_type("Hello"))
    print(what_type(False))


if __name__ == '__main__':
    main()
