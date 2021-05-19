# @desc Triangle practice
# @desc by Bernie '21

def pythagSolve(side_A, side_B):
    side_A = side_A ** 2
    side_B = side_B ** 2
    side_C= (side_A + side_B) ** 0.5
    return  side_C


def main():
    print(pythagSolve(8, 6))
    print(pythagSolve(3, 4))
    print(pythagSolve(4, 3))
    print(pythagSolve(5, 12))

if __name__ == '__main__':
    main()