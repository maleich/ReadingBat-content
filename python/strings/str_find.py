# @desc Finding characters in a string

def find_it(text):
    index = text.find("a")
    return index


def main():
    print(find_it('Anna'))
    print(find_it('marsupial'))
    print(find_it(' orchestra'))
    print(find_it('Mt. Diablo'))
    print(find_it(' Avocado '))

if __name__ == '__main__':
    main()
