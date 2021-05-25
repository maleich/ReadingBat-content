# @desc Determine the value returned by the function?
# @desc by Merrick '23

def word_length(x):
    counter = 0
    for i in x:
        counter += 1
    return counter


def main():
    print(word_length("Sunset"))
    print(word_length("School"))
    print(word_length("Python"))
    print(word_length("Mathematics"))
    print(word_length("Hey"))


if __name__ == '__main__':
    main()

