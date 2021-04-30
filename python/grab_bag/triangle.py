# @desc Can a triangle be made by these sides? By Jake '24

def form_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False


def main():
    print(form_triangle(10, 5, 25))
    print(form_triangle(3, 4, 5))
    print(form_triangle(6, 2, 7))
    print(form_triangle(12, 6, 5))
    print(form_triangle(8, 19, 20))


if __name__ == '__main__':
    main()
