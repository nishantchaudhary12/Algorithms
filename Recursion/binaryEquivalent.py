#binary equivalent


def binary(n):
    if n > 1:
        binary(n // 2)
    print(n % 2, end=' ')


if __name__ == '__main__':
    n = 15
    binary(n)