# @desc Replacing characters in a string

def replace_it(text):
    new_text = text.replace("a", "z")
    return new_text


def main():
    print(replace_it('Anna'))
    print(replace_it('marsupial'))
    print(replace_it('banana'))
    print(replace_it('Mt. Diablo'))
    print(replace_it('Avocado'))

if __name__ == '__main__':
    main()
