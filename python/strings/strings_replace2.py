# @desc Finding characters in a string

def replace_it(text):
    new_text = text.replace("l", "q")
    return new_text


def main():
    print(replace_it('Walla Walla'))
    print(replace_it('lollipop'))
    print(replace_it('animal'))
    print(replace_it('Lemur'))
    print(replace_it('Logically'))

if __name__ == '__main__':
    main()
