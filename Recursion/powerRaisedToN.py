#function for X raised to n


def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, n-1)
    else:
        return 1/x * power(x, n+1)


if __name__ == '__main__':
    x = 5
    n = 3
    print(power(x, n))