# @desc Converting string cases

def case(name):
    if "A" in name:
        return name.upper()
    elif "e" in name:
        return name.lower()
    else:
        return name.title()


def main():
    print(case('Anna'))
    print(case('MIGUEL'))
    print(case('FRed'))
    print(case('Mr. Rodgers'))
    print(case('oliVia'))

if __name__ == '__main__':
    main()
