#factorial of a positive integer


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    n = 0
    print(factorial(n))