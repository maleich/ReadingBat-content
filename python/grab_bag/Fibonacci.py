# @desc Fibonacci problem. By Benji '24

def fibonacci(n):
    a = 1
    prev = 0
    cur = 1
    while a <= n:
        next = prev + cur
        prev = cur
        cur = next
        a += 1
    return cur


def main():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(6))
    print(fibonacci(9))


if __name__ == '__main__':
    main()
