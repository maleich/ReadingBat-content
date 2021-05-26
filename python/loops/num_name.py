# @desc What is returned?
# @desc by Savonnah '23

def num_name(word, x):
    result = 0
    for i in word:
        if i == x:
            result += 1
    return result

def main():
    print(num_name('cheese', 'e'))
    print(num_name('cat', 'z'))
    print(num_name('pink jeans', ' '))
    print(num_name('waterbottle', 't'))


if __name__ == '__main__':
    main()
