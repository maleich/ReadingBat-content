# @desc Predict the returned value
# @desc by Tracy '23

def return_elements_in_lists(x):
    list1 = ['red','yellow','orange','grey','green','purple','blue']
    list2 = ['computer','calculator','cellphone','keys','ipad','stylus']
    if x % 2 == 0:
        return list1[x]
    else:
        return list2[x-1]



def main():
    print(return_elements_in_lists(2))
    print(return_elements_in_lists(3))
    print(return_elements_in_lists(5))
    print(return_elements_in_lists(1))
    print(return_elements_in_lists(6))


if __name__ == '__main__':
    main()