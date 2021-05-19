# @desc Determine the value returned by the function.
# @desc by Bernie '21

def count_int(paramlist):
    num=0
    length=len(paramlist)
    for i in range(length):
        txt=paramlist[i]
        if type(txt) is int:
            num += 1
    return num


def main():
    print(count_int([5, 10, "hi"]))
    print(count_int([14.6, "watermelon", "fish"]))
    print(count_int([-1, 11, 56]))
    print(count_int(["Pangolin", 10, "Catfish"]))




if __name__ == '__main__':
    main()