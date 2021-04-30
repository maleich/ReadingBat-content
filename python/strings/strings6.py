# @desc Splitting a word from another word
# @desc by Savonnah '23

def split(word1, word2):
    result = word1.rstrip(word2)
    return result


def main():
    print(split('carwash', 'wash'))
    print(split('strawberry', 'berry'))
    print(split('hotdog', 'dog'))
    print(split('hamburger', 'burger'))


if __name__ == '__main__':
    main()