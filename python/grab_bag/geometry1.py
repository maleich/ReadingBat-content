# @desc Add a short description or instruction here. This will show up at the top of the exercise.

def pythagSolve(side_A, side_B):     # give your function a name and parameter(s)
    side_A = side_A ** 2
    side_B = side_B ** 2
    side_C= (side_A+side_B) ** 0.5
    return  side_C  # what does it return? This will be what the user types when they predict the result.


def main():
    print(pythagSolve(1, 1))
    print(pythagSolve(3, 4))
    print(pythagSolve(4, 3))
    print(pythagSolve(5, 12))

if __name__ == '__main__':
    main()