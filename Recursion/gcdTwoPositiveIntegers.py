#GCD of two positive integers


def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


if __name__ == '__main__':
    m = 100
    n = 30
    print(gcd(m, n))