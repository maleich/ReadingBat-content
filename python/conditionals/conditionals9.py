# @desc Predict the returned value
# @desc by Merrick '23

def range_checker(x):
    if x < 10:
        return("In range")
    else:
        return("Too large")



def main():
    print(range_checker(5))
    print(range_checker(10))
    print(range_checker(1))
    print(range_checker(20))
    print(range_checker(-1))



if __name__ == '__main__':
    main()
