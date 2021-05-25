# @desc Determine if a is even or odd
# @desc by Tracy '23

def even_or_odd(a):     # give your function a name and parameter(s)
    if a % 2 == 0:
        return ('even') # what does it return? This will be what the user types when they predict the result.
    else:
        return ('odd')

def main():
    print(even_or_odd(5))
    print(even_or_odd(-1))
    print(even_or_odd(0))
    print(even_or_odd(6))
    print(even_or_odd(5 + 3))
    print(even_or_odd(61 - 6))


if __name__ == '__main__':
    main()
